# ShoppingCart class PyTest (unit-testing):

> source: https://www.youtube.com/watch?v=YbpKMIUjvK8   (pixegami)

> mock example was taken from: https://docs.python.org/3/library/unittest.mock.html

> TBD try to find tutorial of how to make a better looking README.md report

# pytest-cov:

> Python lib (pytest-cov) added to requirements.txt enabling to get the coverage report,
> for understanding what coverage of the code lines a specific test suite file went through.
> See example report when runnig: **"pytest --cov"**: *(can also go w/ the full known report: pytest --cov -v)*

>	Name                               Stmts   Miss  Cover
>	------------------------------------------------------
>	item_database.py                       5      1    80%
>	shopping_cart.py                      28      0   100%
>	test_shopping_cart_perplexity.py      38      3    92%
>	test_shoppint_cart.py                 58      0   100%
>	------------------------------------------------------
>	TOTAL                                129      4    97%

## Addition optional args:

> - **pytest --cov=test_shopping_cart_perplexity**   (for running a single test file)
> - **pytest --cov=test_shopping_cart_perplexity** --cov=test_shoppint_cart (running multiple files)

> - **pytest --cov=. --cov-report=term-missing**   (issue report on all files w/ the missing lines - see below example)
> - **pytest --cov=shopping_cart --cov-report=term-missing**   (issue report on a file of interest w/ the missing lines - see the following example)
> - **pytest --cov=. --cov-report=html  --cov-report=term-missing**   (issue an informative report in a lovely HTML format - w/ links)
> - **pytest --cov=shopping_cart --cov-report=term-missing test_shopping_cart.py**   (issue report on the coverage of shopping_cart.py by test_shopping_cart.py file)



## Examplple report *(looks better in the IDE)*:

>	Name                               Stmts   Miss  Cover   Missing  
>	----------------------------------------------------------------  
>	item_database.py                       5      2    60%   6, 10    
>	shopping_cart.py                      28      4    86%   53-57    
>	stam.py                                1      1     0%   1        
>	test_shopping_cart_perplexity.py      38      3    92%   9, 12, 24
>	test_shoppint_cart.py                 41      0   100%            
>	----------------------------------------------------------------  
>	TOTAL                                113     10    91%            


>	Name               Stmts   Miss  Cover   Missing
>	------------------------------------------------
>	shopping_cart.py      28      4    86%   53-57
>	------------------------------------------------
>	TOTAL                 28      4    86%

> note that in the main tested file, shopping_cart.py, there is get_total_price() function that was grayed-out/ignored in both "test_..." files