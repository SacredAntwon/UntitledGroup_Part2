import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import argparse



# helper function for creating bag of words


def create_soup(x):
    result = x['Anime Title']

    if x['Studio'] != 'n/a':
        result += ' ' + x['Studio']
    if x['Source Material'] != 'n/a':
        result += ' ' + x['Source Material']
    if x['Genre'] != 'n/a':
        result += ' ' + x['Genre']
    if x['VAs'] != 'n/a':
        result += ' ' + x['VAs']

    punc = '[],\'\"'

    for ele in result:
        if ele in punc:
            result = result.replace(ele, "")

    return result

# helper function for recommendation algorithms


def get_recs(title, cosine_sim, num, out_list):
    text = "The following are recommendations for "

    # write to file
    with open(out_list, "a+") as f:

        # get the index of the anime that matches the id
        id2 = '\'' + title + '\''
        try:
            idx = (df.loc[df['Anime Title'] == id2].index[0])
        except:
            print("That id does not exist.")
            exit(-1)

        # find sim score of the inputed anime with all other animes
        sim_scores = list(enumerate(cosine_sim[idx]))

        # sort based on sim scores desc
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

        # get recommended animes index
        anime_indices = [i[0] for i in sim_scores]
        if num > 100:
            print('Number of recommendations cannot exceed 100.')
            num = 100
        for i in range(len(sim_scores)):
            if i > num:
                break
            else:
                link = "https://myanimelist.net/anime/"
                temp_id = df.loc[sim_scores[i][0]]["Id"]
                temp_id = temp_id.replace('\'', '')
                link += str(temp_id)

                if i == 0:
                    text += str(df['Anime Title'].iloc[anime_indices[i]])
                    print("%s %s" %
                          (df['Anime Title'].iloc[anime_indices[i]], link))
                    f.write("%s\n%s %s %s\n" % (
                        text, df['Anime Title'].iloc[anime_indices[i]], link, sim_scores[i][1].round(4)))
                else:
                    print("%s %s" %
                          (df['Anime Title'].iloc[anime_indices[i]], link))
                    f.write("%s %s %s\n" % (
                        df['Anime Title'].iloc[anime_indices[i]], link, sim_scores[i][1].round(4)))

        return df['Anime Title'].iloc[anime_indices]

def similarity():
    # read csv file into dataframe
    df = pd.read_csv('top_and_bottom_anime.csv')
    # print(df.shape)

    # preprocessing the csv file
    data = range(len(df))
    for title in data:
        if df.loc[title]['VAs'] == ' \'\'':
            df = df.drop(labels=title, axis=0)

    # make a bag of words csv from database of animes
    df['soup'] = df.apply(create_soup, axis=1)
    df.to_csv("anime_soup.csv", index=None)

    # cosine similarity algorithm
    count = CountVectorizer()
    count_matrix = count.fit_transform(df['soup'])
    count_matrix.shape

    cosine_sim2 = cosine_similarity(count_matrix, count_matrix)
    df = df.reset_index()

    return cosine_sim2, df

# read csv file into dataframe
df = pd.read_csv('top_and_bottom_anime.csv')

if __name__ == "__main__":
    # reading in arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('--number_of_recs', type=int, default=10)
    parser.add_argument('--anime_title', type=str)
    parser.add_argument('--in_list')
    parser.add_argument('--out_list', default="anime.txt")
    args = parser.parse_args()

    if args.anime_title or args.in_list:
        cosine_sim2, df = similarity()

        titles = []
        if args.in_list:
            with open(args.in_list, 'r') as f:
                for line in f:
                    temp_line = line.split()
                    for name in temp_line:
                        titles.append(name)
            for title in titles:
                get_recs(title, cosine_sim2, args.number_of_recs, args.out_list)
        else:
            get_recs(args.anime_title, cosine_sim2, args.number_of_recs, args.out_list)
    else:
        raise Exception(
            "python ./anime.py --number_of_recs <number> --anime_id <id number> --in_list <input file name> --out_list <output file name>")
