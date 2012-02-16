fixbib.py is a  small script that fixes the BibTeX output from [Papers 2](http://www.mekentosj.com/papers/).

Use it by giving the .bib file you want to process as the argument to the script. The script will output the results to standard output. So e.g. if you want to process the file refs.bib and save the results to refs-fixed.bib you would use the following command:

    % fixbib.py refs.bib > refs-fixed.bib

fixbib.py opens the file as utf-8 and writes as utf-8.
