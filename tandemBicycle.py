# Tandem Bicycle
# Time Complexity: O(nlog(n)) || Space Complexity O(1)
def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
    redShirtSpeeds.sort()
    blueShirtSpeeds.sort()
    if not fastest:
        reverseArray(redShirtSpeeds)
    fastestSpeed = 0
    for idx in range(len(redShirtSpeeds)):
        rider1 = redShirtSpeeds[idx]
        rider2 = blueShirtSpeeds[len(blueShirtSpeeds) - 1 - idx]
        fastestSpeed += max(rider1, rider2)
    return fastestSpeed

def reverseArray(array):
    start = 0
    end = len(array) - 1
    while start < end:
        array[start], array[end] = array[end], array[start]
        start += 1
        end -= 1
    
    