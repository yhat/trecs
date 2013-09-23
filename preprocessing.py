from bs4 import BeautifulSoup
import pprint as pp


def get_locs(t):
    top = int(t['top'])
    bottom = top + int(t['height'])
    left = int(t['left'])
    return {"top": top, "bottom": bottom, "left": left}


def main():
    soup = BeautifulSoup(open("../html/pdftohtml_DangerousDog_map.xml").read())

    lines = []

    for t in soup.find_all("text"):
        if not lines:
            lines.append([t])
            continue
        else:
            pl = lines[-1][-1]

        pl = get_locs(pl)
        line = get_locs(t)
        if (line['top'] <= pl['bottom'] and line['top'] >= pl['top']) or (line['bottom'] <= pl['bottom'] and line['bottom'] >= pl['top']):
            lines[-1].append(t)
        else:
            lines.append([t])
    return lines

if __name__=="__main__":
    lines = main()
    for line in lines:
        for item in line:
            print item.text,
        print
        print "*"*80