class Solution(object):
    def findDuplicate(self, paths):
        """
        :type paths: List[str]
        :rtype: List[List[str]]
        """
        d = defaultdict(list)

        for s in paths:             
            s = s.split(' ')                # parse the string: first component is   
            path = s.pop(0)                 # the path; the other components are files

            for file in s:
                idx = file.index('(')       # Build a dict of files with key = file content
                d[file[idx:]].append(path+'/'+file[:idx]) 

                                            # return the dict values for keys w/ > 1 files
        return [d[i] for i in d.keys() if len(d[i]) > 1]