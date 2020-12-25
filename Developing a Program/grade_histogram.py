import tkinter.filedialog # We want user to open any file
import grade # function-only file

al_filename = tkinter.filedialog.askopenfilename()
al_file = open(al_filename, 'r')

al_histfilename = tkinter.filedialog.asksaveasfilename()
al_histfile = open(al_histfilename, 'w')

# Read the grades into a list.
grades = grade.read_grades(al_file)

# Count the grades per range
range_counts = grade.count_grade_ranges(grades)

# Write the histogram to the file
grade.write_histogram(range_counts, al_histfile)

al_file.close()
al_histfile.close()
