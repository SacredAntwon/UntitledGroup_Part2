# About the Project

Anime Recommendation System is a Python script that allow users to input an anime title id as indexed in
our scraped from MAL dataset and give recommendations based on cosine similarity.

This version will include bug fixes, improvements, and unit testing.

# Getting Started

## Requirements

- sci-kit learn
- pandas
  `pip install -r requirements.txt`

## Installation

1. Clone the repo
   `git clone https://github.com/ptreavn/254project`
2. Install the requirements
   `pip install -r requirements.txt`

# Usage

`python ./anime.py --number_of_recs <number> --anime_title <title name> --in_list <input file name> --out_list <output file name>`

- number_of_recs is optional, it changes the number of recommendations you may want for each anime
- anime_title is NOT optional, this is the id of the anime you want recommendations for
- in_list is optional, this is a txt file with multiple ids of animes that you want recommendations for
  > The format of the txt file should be the ids followed by a space e.g. "id id id" _or_ one id per line
- out_list is optional, this is a txt file that you may want your recommendations to be outputted too, default will create and append to file "anime.txt"

# Roadmap

- [x] Add Changelog
- [x] Better Readme
- [x] Names for input instead of id only

# Contributing

**If you have a suggestion that would make this better, please fork the repo and create a pull request.**

1. Fork the Project
2. Create a new Feature Branch ( git checkout -b feature/BranchName)
3. Commit your changes ( git commit -m 'Add some BranchName' )
4. Push to the Branch ( git push origin feature/BranchName )
5. Open a Pull Request

# License

Distributed under the GNU General Public License. See License.md for more information.

# Contact

Kevin Le - kevinle1462@csu.fullerton.edu
Peter Van - ptreavn@csu.fullerton.edu

Modifying Team:

Anthony Maida - amaida@csu.fullerton.edu

Daniel VanDenEykel - d.vandeneykel@csu.fullerton.edu
