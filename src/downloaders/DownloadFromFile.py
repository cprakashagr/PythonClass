import csv
import os
import urllib.request


def reporthook(a, b, c):
    message = "% 3.1f%% of %d bytes\r" % (min(100, float(a * b) / c * 100), c)
    # sys.stdout.write('\r' + message + ' ' * 20)
    # sys.stdout.flush()


def main():
    baseUrl = 'http://s3-us-west-2.amazonaws.com/greedygamemedia/'
    savePath = '/Users/cprakashagr/Pictures/GreedyGame/'
    files = csv.reader(open('/Users/cprakashagr/Pictures/GreedyGame/Playground.csv'), delimiter=' ')
    for row in files:
        for file in row:
            url = baseUrl+file
            saveFile = os.path.join(savePath, file.replace('/', '_'))
            if not os.path.exists(saveFile):
                try :
                    urllib.request.urlretrieve(url, filename=saveFile)
                except:
                    print(file)

    print('Done with all.')


if __name__ == '__main__':
    main()
