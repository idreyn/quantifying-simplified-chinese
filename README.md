# explore-simplified-chinese

This is a collection of experiments in quantifying the differences between traditional and simplified chinese. Specifically it uses stroke count as a measure of character complexity, and rarity as a measure of entropy. The goal is to quantify the efficiency of the two writing systems as encodings for the language in an information-theoretic sense. It makes use of [Shentan](http://github.com/idreyn/shentan), a Chinese dictionary utility of mine.

I plan to write more about this later. In the meantime, if you want to run this code, you'll need `requests`, `click` and `unicodecsv` along with `numpy`, `scipy`, and `matplotlib`. Don't forget to `git submodule init` and `git submodule update`!
