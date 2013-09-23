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

def main():
    soup = BeautifulSoup(open("xml/dangerous_dog.xml").read())
    all_tags = soup.find_all("text")
    Line_els = []

    for tag in all_tags:
        new_text = Text_el()
        for key,value in tag.attrs.iteritems():
            setattr(new_text, key, int(value))
        setattr(new_text, 'text', tag.text)

        Line_els.append(new_text)

    return Line_els

if __name__=="__main__":
    lines = main()
    print vars(lines[0])
