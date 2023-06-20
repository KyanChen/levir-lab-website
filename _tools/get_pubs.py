import os

t = '''Zhi-an Liang and Zhen-wei Shi. Optimality conditions and duality for a minimax fractional programming with generalized convexity. Journal of Mathematical Analysis and Applications, Volume 277, Issue 2, 15 January 2003, pp. 474-488.

'''

date = 2003
t = t.strip().split('\n')
t = [i.strip() for i in t if len(i.strip()) > 1]

totoal = 1+ 90-79
total_tmp = 0
for i in t:
    save_data = '''---
    title: Continuous Remote Sensing Image Super-Resolution based on Context Interaction in Implicit Function Space
    authors: Keyan Chen, Wenyuan Li, Sen Lei, Jianqi Chen, Xiaolong Jiang, Zhengxia Zou, and **Zhenwei Shi**
    journal: IEEE Transactions on Geoscience and Remote Sensing (TGRS)
    pub_date: 2023-05-02
    pdf: /static/pdfs/2023_cky_funsr.pdf
    arxiv: https://arxiv.org/abs/2302.08046
    code: https://github.com/KyanChen/FunSR
    page: https://kyanchen.github.io/FunSR/
    demo: https://huggingface.co/spaces/KyanChen/FunSR
    paper: https://ieeexplore.ieee.org/document/10114420
    bibtex: /static/bib/2023_cky_funsr.txt
    data:
---
    '''

    i = i.split('[')[0].strip()
    i = i.split('doi')[0].strip()
    i = i.split('DOI')[0].strip()
    i = i.split('Volume')[0].strip()
    i = i.split('vol.')[0].strip()
    i = i.split('Vol.')[0].strip()
    i = i.split('pp.')[0].strip()
    i = i.split('no.')[0].strip()
    split_text = i.split('.')
    split_text = [x for x in split_text if len(x.strip()) > 1]
    if len(split_text) == 3:
        authors = split_text[0].strip()
        title = split_text[1].strip()
        authors = authors.replace('Zhenwei Shi', '**Zhenwei Shi**')
        journal = split_text[2].strip()
        journal = journal.split(',')[0].strip()
        save_data = save_data.replace('Continuous Remote Sensing Image Super-Resolution based on Context Interaction in Implicit Function Space', f'"{title}"')
        save_data = save_data.replace('Keyan Chen, Wenyuan Li, Sen Lei, Jianqi Chen, Xiaolong Jiang, Zhengxia Zou, and **Zhenwei Shi**', authors)
        save_data = save_data.replace('IEEE Transactions on Geoscience and Remote Sensing (TGRS)', journal)
        save_data = save_data.replace('2023-05-02', str(date) + '-01-01')
        save_data = save_data.replace('arxiv: https://arxiv.org/abs/2302.08046', 'arxiv: ')
        save_data = save_data.replace('code: https://github.com/KyanChen/FunSR', 'code: ')
        save_data = save_data.replace('page: https://kyanchen.github.io/FunSR/', 'page: ')
        save_data = save_data.replace('demo: https://huggingface.co/spaces/KyanChen/FunSR', 'demo: ')
        save_data = save_data.replace('paper: https://ieeexplore.ieee.org/document/10114420', 'paper: ')

        f_author = authors.split(',')[0].strip().lower().replace(' ', '_')
        f_name = title.split(' ')[0].strip().lower()
        name = f'{date}_{f_author}_{f_name}'
        save_data = save_data.replace('pdf: /static/pdfs/2023_cky_funsr.pdf', f'pdf: /static/pdfs/{name}.pdf')
        save_data = save_data.replace('bibtex: /static/bib/2023_cky_funsr.txt', f'bibtex: /static/bib/{name}.txt')
    else:
        print(i)
        print('error')
    os.makedirs(f'extra/pub', exist_ok=True)
    with open(f'extra/pub/{name}.md', 'w') as f:
        f.write(save_data)
    os.makedirs(f'extra/pdf', exist_ok=True)
    with open(f'extra/pdf/{name}.pdf', 'w') as f:
        pass
    os.makedirs(f'extra/bib', exist_ok=True)
    with open(f'extra/bib/{name}.txt', 'w') as f:
        pass
    total_tmp += 1

print(total_tmp)
print(totoal)

