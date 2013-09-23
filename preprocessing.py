from bs4 import BeautifulSoup
import pprint as pp


def get_locs(t):
    top = int(t['top'])
    bottom = top + int(t['height'])
    left = int(t['left'])
    return {"top": top, "bottom": bottom, "left": left}

class Text_el:
    def __init__(self):
        self.top = "_"
        self.left ="_"
        self.width ="_"
        self.height ="_"
        self.font ="_"
        self.text ="_"
    
    @property
    def bottom(self):
        return self.top + self.height

def main():
    soup = BeautifulSoup(open("xml/dangerous_dog.xml").read())
    all_tags = soup.find_all("text")
    text_els = []

    for tag in all_tags:
        new_text = Text_el()
        for key,value in tag.attrs.iteritems():
            setattr(new_text, key, int(value))
        setattr(new_text, 'text', tag.text)

        text_els.append(new_text)

    lines = make_lines(text_els)
    print [[txt.text for txt in line] for line in lines]
    for line in lines:
        num_text_el=0
        for item in line:
            num_text_el+=1
            print item.text, 
        print num_text_el
        print
        print "*"*80
    1/0

    return text_els


def make_lines(text_els):
    sorted_text_els = sorted(text_els, key=lambda text_el: text_el.top)
    lines = []
    line = []
    current_line_bottom = 0
    num_prev_text = 0
    for text_el in sorted_text_els:
        if len(line)==0: #start new line
            line.append(text_el)
            current_line_bottom = text_el.bottom
        else: #check if text_el overlaps with last line
            if text_el.top < current_line_bottom:
                line.append(text_el)
                if text_el.bottom < current_line_bottom:
                    current_line_bottom = text_el.bottom
            else: # save line to lines and start new
                # check if last line had <6 and if this line has less, if so then merge
                #print current_line_bottom-text_el.top
                if num_prev_text >= 6 and len(line) <6 and distance > -20:
                    print "merging", lines[-1][0].text, "with", line[0].text, distance
                    lines[-1] += line
                else:
                    lines.append(line)
                num_prev_text = len(line)
                line=[text_el]
                distance = current_line_bottom-text_el.top 
                current_line_bottom = text_el.bottom

    return lines


if __name__=="__main__":
    lines = main()
    print vars(lines[0])
