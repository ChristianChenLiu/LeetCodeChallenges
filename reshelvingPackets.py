def reshelvingPackets(packets):
    sortedPackets = sorted(packets)
    packetToShelf = {}
    currentShelf = 1
    for packet in sortedPackets:
        if packet not in packetToShelf:
            packetToShelf[packet] = currentShelf
            currentShelf += 1
    res = []
    for packet in packets:
        res.append(packetToShelf[packet])
    return res