import os
import random
import re
import sys

DAMPING = 0.85
SAMPLES = 10000

sys.argv.append("corpus0")
def main():
    #if len(sys.argv) != 2:
        #sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages
        )

    return pages


def transition_model(corpus, page, damping_factor):
    """
    Return a probability distribution over which page to visit next,
    given a current page.

    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.
    """
    links = corpus[page]
    if not links:
        links = corpus.keys()
    # evenly likely
    probs = dict.fromkeys(
        corpus,
        (1 - (damping_factor if links else 0))/len(corpus)
    )
    
    # + probs for links
    for link in links:
        probs[link] += damping_factor/len(links)
    
    return probs


def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    # random initial page
    page = random.choice(list(corpus.keys()))
    ranks = dict.fromkeys(corpus, 0)

    # start the chain
    for i in range(n):
        # pick
        probs = transition_model(corpus, page,damping_factor)
        page = random.choices(list(probs.keys()), weights=probs.values())[0]
        
        # rank
        ranks[page] += 1/n
        
    return ranks


def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    ranks = dict.fromkeys(corpus, 1/len(corpus)) # evenly
    
    # iterate untill convergence
    while True:
        new = {}
        for page in corpus:
            # sigma of probs by links to page
            sigma = 0
            for linking_page in corpus:
                if (page in corpus[linking_page] or not corpus[linking_page]) and linking_page != page: 
                    num_links = len(corpus[linking_page]) or len(corpus)
                    sigma += ranks[linking_page] / num_links
                    
            # new rank
            new[page] = (1 - damping_factor) / len(corpus) + damping_factor * sigma
            
        # if converged:
        if all(abs(new[p] - ranks[p]) < 0.001 for p in corpus):
                return new
                
        ranks = new


if __name__ == "__main__":
    main()