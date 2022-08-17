from typing import List

""" You are given a list of files. You need to sort this list by the file extension. 

Some possible cases:
  The files with the same extension should be sorted by name.
  Filename cannot be an empty string
  Files without the extension should go before the files with one
  Filename ".config" has an empty extension and a name ".config"
  Filename "config." has an empty extension and a name "config."
  Filename "table.imp.xls" has an extension "xls" and a name "table.imp"
  Filename ".imp.xls" has an extension "xls" and a name ".imp".

Input: A list of filenames.

Output: A list of filenames. """

# Understand the problem:

#  You need to sort the list of files by the file extension. Example: ['1.cad', '1.bat', '1.aa', '2.bat'] -> ['1.aa', '1.bat', '2.bat', '1.cad']

#  Cases:
#   1. The files with the same extension should be sorted by name. Example: ["2.bat", "1.bat"] -> ["1.bat", "2.bat"]
#   2. Files without the extension should go before the files with one. Example: ['1.cad', '1.bat', '.aa', '.bat'] -> ['.aa', '.bat', '1.bat', '1.cad']

#  Algorithm:
#  1. Sort the array of strings based on the extension using a comparator function.
#  2. Files without the extension should go before the files with one
#  3. If the extension is the same, sort the array based on the name.
#  4. print the sorted array.


def file_key(file):
    name, dot, extension = file.rpartition('.')
    return (extension, name) if name and extension else ('', file)


def sort_by_ext(files: List[str]) -> List[str]:
    return sorted(files, key=file_key)


if __name__ == '__main__':
    print("Example:")
    print(sort_by_ext(['1.cad', '1.bat', '1.aa']))

    assert sort_by_ext(['1.cad', '1.bat', '1.aa']) == [
        '1.aa', '1.bat', '1.cad']
    assert sort_by_ext(['1.cad', '1.bat', '1.aa', '2.bat']) == [
        '1.aa', '1.bat', '2.bat', '1.cad']
    assert sort_by_ext(['1.cad', '1.bat', '1.aa', '.bat']) == [
        '.bat', '1.aa', '1.bat', '1.cad']
    assert sort_by_ext(['1.cad', '1.bat', '.aa', '.bat']) == [
        '.aa', '.bat', '1.bat', '1.cad']
    assert sort_by_ext(['1.cad', '1.', '1.aa']) == ['1.', '1.aa', '1.cad']
    assert sort_by_ext(['1.cad', '1.bat', '1.aa', '1.aa.doc']) == [
        '1.aa', '1.bat', '1.cad', '1.aa.doc']
    assert sort_by_ext(['1.cad', '1.bat', '1.aa', '.aa.doc']) == [
        '1.aa', '1.bat', '1.cad', '.aa.doc']
    print("Coding complete!")
