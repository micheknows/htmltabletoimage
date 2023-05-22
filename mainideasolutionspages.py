from html2image import html2image
import random

class mainideasolutionspages:

    def __init__(self):
        self.htmlimg = html2image.Html2Image()
        self.htmlimg.output_path = "htmlimages"

    # This method will create the multiple choice recording and solutions page.
    # No output but it creates a file with the given filename for output
    # INPUT:
    #  output : filename to save image
    #  startingnum : the number to start with (defaults at 1)
    #  endingnum : the number to end with (defaults at 12)
    #  choices : list of dictionaries of choices for each question  ({correct:text, choice1:text, choice2:text}, etc)
    def mcsolutions(self, output='my_img.png', startingnum=1, endingnum=12, choices=[], keys=False):
        html = "<h1 class='centered'>MAIN IDEA TASK CARDS</H1>"
        html += "<h2 class='centered'>Answer Sheet for Cards 1-12 <br> Use this chart to record your answers.</h2>"
        if (keys):
            html += "<h2 class='centered' style=\"color:red;\"> KEY </h2>"
        css = 'body {background-color:white;} .centered {text-align: center} .border {border: 1px solid black;border-collapse: collapse;padding:10px}'
        filesize = (1008, 768)
        # create two tables with a border
        # create outer table without border
        html += '<P><table style=\"width:100%\"><tr><td>'

        # create 2 inner tables
        for x in range(2):
            # create table and headers
            html += '<table class=\"border\" style=\"width:100%\"><tr class=\"border\"><th>Card #</th><th>Select the main idea</th</tr>'

            for y in range(startingnum, startingnum + 6):
                html += "<tr class='border'><td class='border'>" + str(y) + "</td><td>a.  "
                # save temp choices

                temp_choices = []
                names = ['correct', 'choice1', 'choice2']
                for j in range(3):
                    if (random.randint(0, 1)):
                        if (keys and (names[j] == 'correct')):
                            temp_choices.insert(0, "<span style=\"color:red;\">" + choices[startingnum - y][
                                names[j]] + "</span>")
                        else:
                            temp_choices.insert(0, choices[startingnum - y][names[j]])
                    else:
                        if (keys and (names[j] == 'correct')):
                            temp_choices.append(
                                "<span style=\"color:red;\">" + choices[startingnum - y][names[j]] + "</span>")
                        else:
                            temp_choices.append(choices[startingnum - y][names[j]])

                for j in range(3):
                    if (j == 1):
                        html += "<br>b.  "
                    if (j == 2):
                        html += "<br>c.  "
                    html += temp_choices[j]

                html += "</td></tr>"
            startingnum += 6

            # end inner table
            html += "</td></tr></table>"
            # move to second inner table
            html += "</td><td>"

        # end the outer table
        html += "</td></tr></table>"

        # save to image
        self.htmlimg.screenshot(
            html_str=html,
            css_str=css,
            save_as=output,
            size=filesize

        )

    # This method will create the multiple choice recording and solutions page.
    # No output but it creates a file with the given filename for output
    # INPUT:
    #  output : filename to save image
    #  startingnum : the number to start with (defaults at 1)
    #  endingnum : the number to end with (defaults at 12)
    #  choices : list of dictionaries of choices for each question  ({correct:text, choice1:text, choice2:text}, etc)

    def writesolutions(self, output='my_img.png', startingnum=1, endingnum=12, choices=[], keys=False):
        html = "<h1 class='centered'>MAIN IDEA TASK CARDS</H1>"
        html += "<h2 class='centered'>Answer Sheet for Cards 1-12 <br> Use this chart to record your answers.</h2>"
        if (keys):
            html += "<h2 class='centered' style=\"color:red;\"> KEY </h2>"
        css = 'body {background-color:white;} .centered {text-align: center} .border {border: 1px solid black;border-collapse: collapse;padding:10px}'
        filesize = (1008, 768)

        # create outer table without border
        html += '<P><table class=\"border\" style=\"width:100%\"><tr><td>'
        for y in range(startingnum, startingnum + 12):
            html += "<tr class='border'><td class='border' width=\"5%\">" + str(y) + "</td><td> "
            if(keys):
                html += "<span style=\"color:red;\">" + choices[startingnum - y]['correct'] + "</span>"

            html += "</td></tr>"


        # end the outer table
        html += "</td></tr></table>"

        # save to image
        self.htmlimg.screenshot(
            html_str=html,
            css_str=css,
            save_as=output,
            size=filesize

        )




mis = mainideasolutionspages()
choices = [
    {'correct' : 'Hares and rabbits are not the same',
     'choice1' : 'Hares are bigger than rabbits',
     'choice2' : 'Rabbits live together in burrows'},
    {'correct' : 'Hares and rabbits are not the same',
     'choice1' : 'Hares are bigger than rabbits',
     'choice2' : 'Rabbits live together in burrows'},
    {'correct' : 'Hares and rabbits are not the same',
     'choice1' : 'Hares are bigger than rabbits',
     'choice2' : 'Rabbits live together in burrows'},
    {'correct' : 'Hares and rabbits are not the same',
     'choice1' : 'Hares are bigger than rabbits',
     'choice2' : 'Rabbits live together in burrows'},
    {'correct' : 'Hares and rabbits are not the same',
     'choice1' : 'Hares are bigger than rabbits',
     'choice2' : 'Rabbits live together in burrows'},
    {'correct' : 'Hares and rabbits are not the same',
     'choice1' : 'Hares are bigger than rabbits',
     'choice2' : 'Rabbits live together in burrows'},
    {'correct' : 'Hares and rabbits are not the same',
     'choice1' : 'Hares are bigger than rabbits',
     'choice2' : 'Rabbits live together in burrows'},
    {'correct' : 'Hares and rabbits are not the same',
     'choice1' : 'Hares are bigger than rabbits',
     'choice2' : 'Rabbits live together in burrows'},
    {'correct' : 'Hares and rabbits are not the same',
     'choice1' : 'Hares are bigger than rabbits',
     'choice2' : 'Rabbits live together in burrows'},
    {'correct' : 'Hares and rabbits are not the same',
     'choice1' : 'Hares are bigger than rabbits',
     'choice2' : 'Rabbits live together in burrows'},
    {'correct' : 'Hares and rabbits are not the same',
     'choice1' : 'Hares are bigger than rabbits',
     'choice2' : 'Rabbits live together in burrows'},
    {'correct' : 'Hares and rabbits are not the same',
     'choice1' : 'Hares are bigger than rabbits',
     'choice2' : 'Rabbits live together in burrows'},
]
# DO THE MULTIPLE CHOICE SHEETS
# 1 - 12
mis. mcsolutions(output='sheet1.png',startingnum=1,endingnum=12,choices=choices)
# 13-24
mis. mcsolutions(output='sheet2.png',startingnum=13,endingnum=24,choices=choices)
#DO KEYS
# 1 - 12
mis. mcsolutions(output='key1.png',startingnum=1,endingnum=12,choices=choices, keys=True)
# 13-24
mis. mcsolutions(output='key2.png',startingnum=13,endingnum=24,choices=choices, keys=True)

# DO THE WRITE IN ANSWERS SHEETS
# 1 - 12
mis. writesolutions(output='write1.png',startingnum=1,endingnum=12,choices=choices)
# 13-24
mis. writesolutions(output='write2.png',startingnum=13,endingnum=24,choices=choices)
#DO KEYS
# 1 - 12
mis. writesolutions(output='writekey1.png',startingnum=1,endingnum=12,choices=choices, keys=True)
# 13-24
mis. writesolutions(output='writekey2.png',startingnum=13,endingnum=24,choices=choices, keys=True)