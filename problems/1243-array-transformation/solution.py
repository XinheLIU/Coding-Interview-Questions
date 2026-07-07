class Solution:
    def transformArray(self, arr: List[int]) -> List[int]:
        changed = True
        while changed:
            next = arr[:]
            changed = False

            for i in range(1, len(arr) - 1):

                # Apply rule 1 to next array
                if arr[i] < arr[i-1] and arr[i] < arr[i+1]:
                    next[i] += 1
                    changed = True

                # Apply rule 2 to next array
                elif arr[i] > arr[i-1] and arr[i] > arr[i+1]:
                    next[i] -= 1
                    changed = True

            # Repeat this loop using the next array
            arr = next
        return arr