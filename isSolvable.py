class Solution:
    def isSolvable(self, words: List[str], result: str) -> bool:
        def dfs(nums: set, current_char_index: int, total: int) -> bool:
            # If one character left. Need its multiplier * valid digit in nums to cancel out total
            if current_char_index + 1 == len(chars):
                if total == 0:
                    return (0 in nums and current_char_index not in not_zero_inds)

                my_mult = multiplier[current_char_index]

                return (total % my_mult == 0 and -(total // my_mult) in nums)

            # Exit early if total is too large (negative or positive) to reach 0 in DFS
            if total < 0 and remaining_pos_sum[current_char_index] * max(nums) + total < 0:
                return False
            elif total > 0 and remaining_neg_sum[current_char_index] * max(nums) + total > 0:
                return False

            if current_char_index - 1 in checkpoints:
                reverse_total_string = str(abs(total))[::-1]
                for digit_position in checkpoints[current_char_index - 1]:
                    if digit_position >= len(reverse_total_string):
                        continue
                    if reverse_total_string[digit_position] != '0':
                        return False

            my_mult = multiplier[current_char_index]
            if current_char_index in not_zero_inds and 0 in nums:
                for digit in nums - {0}:
                    if dfs(nums - {digit}, current_char_index + 1, total + digit * my_mult):
                        return True
            else:
                if 0 in nums and dfs(nums - {0}, current_char_index + 1, total):
                    return True
                for digit in nums - {0}:
                    if dfs(nums - {digit}, current_char_index + 1, total + digit * my_mult):
                        return True
            return False

        # 1. Check the lengths of each word and result
        #   First conditional works because no leading zeros.
        #   Second conditional works because len(words) < 10
        longest_word_len = len(max(words, key=len))
        if (len(result) < longest_word_len) or (len(result) > longest_word_len + 1):
            return False

        # 2. Check if result is in words
        #    Last conditional for testcases like words = ['AA', 'AA'], result = 'AA'
        if result in words:
            return len(words) < 3 and all(word == result or len(word) == 1 for word in words) and (
                    len(result) == 1 or words.count(result) < 2)

        # 3. Set of all letters
        chars = set(result)
        for word in words:
            chars.update(set(word))

        # 4. Letters in words add to the total
        multiplier_temp = {char: 0 for char in chars}
        groups = [set() for _ in range(max(longest_word_len, len(result)))]

        for word in words:
            for i, char in enumerate(reversed(word)):
                multiplier_temp[char] += pow(10, i)
                groups[i].add(char)

        # 5. And letters in result subtract from the total
        for i, char in enumerate(reversed(result)):
            multiplier_temp[char] -= pow(10, i)
            groups[i].add(char)

        # 6. Letters that add and subtract the same amount can be any number, so ignore them.
        old_size = len(chars)
        chars = {char for char in chars if multiplier_temp[char] != 0}

        # 7. Update groups if change was made. Crucial to do updates for checkpoints
        if len(chars) != old_size:
            for group in groups:
                group.intersection_update(chars)

        # 8. Check rare case with < 2 chars remaining
        if len(chars) == 0:
            return True

        if len(chars) == 1:
            not_zero_chars = {word[0] for word in words if len(word) > 1}
            if len(result) > 1:
                not_zero_chars.add(result[0])
            return min(chars) not in not_zero_chars

        first_appearance = {}
        for i, group in enumerate(groups):
            for char in group:
                if char not in first_appearance:
                    first_appearance[char] = i

        # 9. Sort characters by first appearance in a group, then by decreasing multiplier size.
        chars = sorted(chars, key=lambda c: first_appearance[c])

        # 10. Get the prefix unions of groups = lowest decimal index of appearance
        for group_index in range(1, len(groups)):
            groups[group_index].update(groups[group_index - 1])

        # 11. Leading letters cannot be zero unless the length of the word is 1
        not_zero_chars = {word[0] for word in words if len(word) > 1}
        if len(result) > 1:
            not_zero_chars.add(result[0])

        # 12. Once a number has been assigned to all the letters in a group
        #     the digit in total at position 10**i must be zero for a solution to exist
        #
        #     For each character, in order of first appearance in groups, if we find a prefix union group
        #     that is a subset of previous characters, i.e. all characters appearing below this place value
        #     are at the start of chars, add the place index to a checkpoint for the character

        not_zero_inds = set()
        checkpoints = {}
        seen = set()
        min_checked = 0
        multiplier = [0] * len(chars)
        for i, char in enumerate(chars[:-1]):
            # Initialize multiplier list and nonzero inds set
            multiplier[i] = multiplier_temp[char]
            if char in not_zero_chars:
                not_zero_inds.add(i)

            seen.add(char)
            for group_index in range(min_checked, len(groups)):
                if groups[group_index].issubset(seen):
                    if i in checkpoints:
                        checkpoints[i].append(group_index)
                    else:
                        checkpoints[i] = [group_index]
                    min_checked = group_index + 1
                else:
                    break

        # 13. Update last index, not reached in above loop
        if chars[-1] in not_zero_chars:
            not_zero_inds.add(len(chars) - 1)
        multiplier[-1] = multiplier_temp[chars[-1]]

        # 14. Get suffix sums of exclusively positive or negative values for DFS pruning
        remaining_pos_sum = [0]*(len(chars)+1)
        remaining_neg_sum = [0]*(len(chars)+1)
        for i, multi_val in enumerate(multiplier):
            if multi_val > 0:
                remaining_pos_sum[i+1] = remaining_pos_sum[i] + multi_val
                remaining_neg_sum[i+1] = remaining_neg_sum[i]
            else:
                remaining_pos_sum[i + 1] = remaining_pos_sum[i]
                remaining_neg_sum[i + 1] = remaining_neg_sum[i] - multi_val

        # 15. Convert prefix sums to suffix sums
        big = remaining_pos_sum[-1]
        remaining_pos_sum = [big-x for x in remaining_pos_sum]
        small = remaining_neg_sum[-1]
        remaining_neg_sum = [x-small for x in remaining_neg_sum]

        return dfs(nums=set(range(10)), current_char_index=0, total=0)