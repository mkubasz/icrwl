# Python engineer test
We hope this task will give you an opportunity to present your knowledge in
Python language as well as general algorithmic knowledge. However, what is even more important to us is that you have fun with it!

## The task
Here is the task to solve:
We would like to create a map of our website: https://globalapptesting.com.
Can you provide us with a tool for creating the map we are interested in?

Here are some more detailed requirements:
* We want to start from the homepage (https://globalapptesting.com) and find any possible transitions between subpages. You may focus only on using links (<a> tags).
* We are interested in the best possible map representation: could you suggest one? <font color="red">Networkx tak jak zrobiliśmy</font>
* We would like to see basic metrics related to our site, namely:
    * What is the distance between the most distant subpages?<font color="red">Już zrobione za pomocą grafu</font>
    * What is the average number of links coming out of subpages of our website to different websites? <font color="red">Średnia ilość linków zewnetrznych na każdej podstronie globaltesting (scrapy extrernal_number) </font>
    * What is the average number of internal links on our website? <font color="red">Średnia ilosć linków wewnetrznych na globaltesting (scrapy internal_number) </font>
    * Average size of the page in our website (HTML only!). <font color="red">Na moje oke walimy razem z js'em czyli response.content
    (scrapy content_len)  </font>
* We would like to know if there are any dead (pointing to the non-existing pages) links on our site. <font color="red">Ja bym to zrobił tak sprawdzamy każdy link i patrzymy jego status jeżeli 400-500 uznajemy go za dead (scrapy url, status, referer)</font>
* We are interested in getting the full path printed on the screen as well as its length. <font color="red">Nie wiem co ćpali, nie rozumiem ich 
full path może pełna sciężka strony, ale nie wiem względem czego?</font>
* We would like to find the pages which are the most difficult to enter (that have the minimal number of incoming links) when using our webpage. <font color="red">Strony (nie wiem czy tylko wewnetrznę czy również zew., ale możemy uznać, że tylko wewnętrzne, do których jest najmniej odnośników/linków?</font>
* We would also like to find pages which are most linked in our website. <font color="red">Najczęsciej występowane linki na stronie?</font>

Consider different approaches (web technologies, map representations etc.) and pick the best one in your opinion.

## Nice to have (optional, not required): <font color="red">Ja to bym zrobił w streamlit jako prosty dashboard z logiką</font>
* We would like to have a text-based UI which allows to ask about the shortest path between two provided subpages (e.g. between https://globalapptesting.com and https://www.globalapptesting.com/customers/facebook)
* We would like to see graphical representation of the subpages of our website and their relations.
* We would like to have the ability to save the generated map and restore it from the file to avoid the need of regenerating the whole map.
