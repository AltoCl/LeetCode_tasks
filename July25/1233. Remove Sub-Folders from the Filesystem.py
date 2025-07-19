# Given a list of folders folder, return the folders after removing all sub-folders in those folders. You may return the answer in any order.
#
# If a folder[i] is located within another folder[j], it is called a sub-folder of it. A sub-folder of folder[j] must start with folder[j], followed by a "/". For example, "/a/b" is a sub-folder of "/a", but "/b" is not a sub-folder of "/a/b/c".
#
# The format of a path is one or more concatenated strings of the form: '/' followed by one or more lowercase English letters.
#
# For example, "/leetcode" and "/leetcode/problems" are valid paths while an empty string and "/" are not.


class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        # Sort the folders lexicographically so parent folders come before their subfolders
        folder.sort()

        # Initialize result list with the first folder
        ans = [folder[0]]

        # Iterate through remaining folders starting from index 1
        for i in range(1, len(folder)):
            # Get the last added folder path and add a trailing slash
            last_folder = ans[-1] + '/'

            # Check if current folder starts with last_folder
            # If it doesn't start with last_folder, then it's not a subfolder
            if not folder[i].startswith(last_folder):
                ans.append(folder[i])

        return ans