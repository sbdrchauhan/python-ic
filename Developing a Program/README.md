I am thankful to [Learn to Program: The Fundamentals](https://www.coursera.org/learn/learn-to-program/home/welcome) for the following knowledge.

**A. Developing a Program**: *From start to finish*

Given: An assignment grades of a class of students. It has 3 lines header, space and then student Id followed by grade.
We are given 'Assignment 1 grades.txt' file that contains our data.
We build: 'a1_hist.txt'

We want: We want to see the distribution of the grades.

To do:

- Read the grades into a list
- Count teh grades per range
- Write the histogram to the file

We make the main program as `grade_histogram.py` while all the functions required to do it in `grade.py` file.

From the beginning, we document, we check the progress and see if program does what we expect. This is crucial, as we progess more and more and if we write 100s of lines of codes and try to check, it will be very troublesome at that point.



**B. Handling Files**:

**Reading Files** (4 ways):

<u>To open a File</u>

`file_object = open(filename, mode)`

<u>mode</u>

`'r'` to read
`'w'` to write
`'a'` to append

`file_object.open(filename, 'r')`
1. The readline way
`file_object.readline()` this reads the first line including `\n` newline character and returns it
If we continue to call `file_object.readline()` it will continue to read the next line in the file. So, if we encounter the `\n` only, it means that we have seen the first empty line in the file and so on. So we could use `while` loop to read in this mode to readline of the file until we see `\n`.

2. The `for` loop way
We could also loop each line of `file_object` like
```python
for line in file_object:
  print(line, end='') # this ensures no extra line space is printed
```

3. The `read` entire file way
`file_object.read()` prints all lines of file at once as a single string including newline characters and every punctuations

4. The readlines way
`file_object.readlines()` readlines returs a list of all lines in a file

*Remember to close all the opened file_objects.close().



**Writing a File**
`file_object.open(filename, 'w')`

<u> To get the path of the file in your computer system </u>

```python
>>> import tkinter.filedialog
>>> from_filename = tkinter.filedialog.askopenfilename() # from this file ( this just gives you path of file )
>>> to_filename = tkinter.filedialog.asksaveasfilename() # save to this file ( this also gives path of file to save )

from_file_object = open(from_filename, 'r')
contents = from_file_object.read()
from_file_object.close()

to_file_object = open(to_filename, 'w')
to_file_object.write("New_changes")
to_file_object.write(contents)
to_file_object.close()
