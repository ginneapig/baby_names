# Annie Gao
# CSc 110, Spring 2017, Section 1C
# HW 6: Baby Names
# 2/28/17

# This program allows input of a name and gender to find the statistics
# of its popularity since whatever year the STARTING_YEAR constant is set at,
# displayed on an adjustable histogram.

from drawingpanel import *     # so that I can use graphics

STARTING_YEAR = 1890    # data withdrawn starts from this year, 1890
DECADE_WIDTH = 60       # decade bars' width in DrawingPanel, 60
RECT_HEIGHT = 30        # height of gray bars of DrawingPanel histogram, 30

# This function includes input of name and gender and accounts for
# the possibility of the inputted name not found in the database of names.
def main():
    introduction()
    name1 = input("Name: ")
    name = name1.lower()
    gender = input("Gender: ")
    gender = gender.lower()
    name_line = find_name("names.txt",name,gender)
    meaning_line = find_name("meanings.txt",name,gender)
    
    if(name_line != ""):
        print(name_line)
        print(meaning_line)
        p = DrawingPanel(780,500+2*RECT_HEIGHT,background="white")
        draw_basics(p,meaning_line)
        draw_histogram(p,name_line)
    else:
        print('"' + name1 + '" not found.')

# This function introduces the user to the program's purpose and range.
def introduction():
    print("This program allows you to search through the")
    print("data from the Social Security Administration")
    print("to see how popular a particular name has been")
    print("since " + str(STARTING_YEAR) + ".")
    print()

# This uses the name, gender, and file name to return a line of information.
def find_name(fname,name,gender):
    fname = open(fname)
    fname = fname.readlines()
    for line in fname:
        lower_line = line.lower().strip().split()
        if(lower_line[0] == name and lower_line[1] == gender[0]):
            name_line = line.strip()
            return name_line
    return ''

# This draws the basic design of the histogram. 
def draw_basics(p,meaning_line):
    p.canvas.create_rectangle(0,0, 785,RECT_HEIGHT, fill="light gray")
    p.canvas.create_rectangle(0,500+RECT_HEIGHT, 785,565, fill="light gray")
    p.canvas.create_text(390,RECT_HEIGHT/2, text = meaning_line)

# This draws the rest of the histogram based on inputted information.
def draw_histogram(p,name_line):
    name_line = name_line.lower().strip().split()   # turns name information into a list
    color = "light green"       # cumulative sum: changing column colors for gender
    if(name_line[1] == "f"):
        color = "yellow"

    for i in range(0,len(name_line)-2):
        # Adds the years on the histogram. 
        p.canvas.create_text(15+DECADE_WIDTH*i,500+2*RECT_HEIGHT-8,
                             text=str(STARTING_YEAR+10*i))


        y1 = RECT_HEIGHT+int(name_line[2+i])/2    # cumulative sum: changing y1 in columns
        if(int(name_line[2+i]) == 0):
            y1 = 500+RECT_HEIGHT

        # Creates columns of varying height indicating popularity in that year.
        p.canvas.create_rectangle(DECADE_WIDTH*i,y1,
                                  DECADE_WIDTH*i+DECADE_WIDTH/2,500+RECT_HEIGHT,
                                  fill=color, width=0)

        # Adds rank on top left corner of corresponding column.
        p.canvas.create_text(DECADE_WIDTH*i,y1, text=str(name_line[2+i]))

main()












