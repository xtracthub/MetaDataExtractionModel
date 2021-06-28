with open('cdiac_naivetruth.csv', 'r') as f:
    for line in f:
        print(line)
        with open('cdiac_naivetruth_processed.csv', 'a+') as g:
            new_line = line.replace('/Users/ryan/Documents/CS/CDAC/official_xtract/sampler_dataset/pub8/', '/home/cc/CDIACPub8/')
            g.write(new_line)