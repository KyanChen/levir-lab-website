# LEVIR Lab
====================

Technologies this website uses:  

    Jekyll  
    Github Pages  
    Twitter Bootstrap 4.4.1

Before pushing changes, please check that they will work on your system first with the plugins included in the Gemfile using the bundler tool (results served at [localhost:4000](localhost:4000)):

    sudo gem install bundler
    bundle install
    bundle exec jekyll serve
    
To create a conda environment to locally test and host, the following should suffice:

    conda create -n jekyll -c conda-forge rb-jekyll
    conda activate jekyll
    bundle install
    bundle exec jekyll serve

How to use the website:

1. clone the repository
2. config the jekyll runtime environment
3. bundle exec jekyll serve
4. download the levir_template.zip from the cms2 management system
5. unzip the levir_template.zip and rename the folder to levir_temp
6. copy the "_site\*" files to the levir_temp\file\_webprj\
7. zip the levir_temp folder to levir_temp.zip and upload to the cms2 management system
8. new a index template in the cms2 management system and copy the index.html content to the template
9. change the index.html to index.jsp in index.jsp file
10. 