MicroGP v4
==========

[![License: Apache 2.0](https://img.shields.io/badge/license-apache--2.0-green.svg)](https://opensource.org/licenses/Apache-2.0) 
[![Status: Actrive](https://img.shields.io/badge/status-active-brightgreen.svg)](https://github.com/squillero/microgp3)
![Language: Python](https://img.shields.io/badge/language-python-blue.svg)
![Version: 4!1.0α1](https://img.shields.io/badge/version-4!1.0α1-orange.svg)
![Codename: kiwi](https://img.shields.io/badge/codename-kiwi-orange.svg)
![](https://www.google-analytics.com/collect?v=1&t=pageview&tid=UA-28094298-5&cid=4f34399f-f437-4f67-9390-61c649f9b8b2&dp=1)

> :warning: MicroGP v4 is currently [**Pre-alpha**](https://en.wikipedia.org/wiki/Software_release_life_cycle#Pre-alpha).

MicroGP (µGP, `ugp`) is an evolutionary optimizer able to outperform both human experts and conventional heuristics in finding the optimal solution of generic problems. It is extremely versatile, being able to tackle problem those solutions are fixed-length bit strings, as well as to optimize realistic assembly programs including loops, interrupts and recursive sub routines.

MicroGP first creates a set of random solutions, then iteratively refines and enhances them using the result of their evaluations together with structural information; [several different techniques](https://scholar.google.com/scholar?q=%28+squillero+OR+tonda+%29+AND+microgp) are used to explore efficiently the search space, and eventually pinpoint the best solution. The first prototype was created [around Y2K](HISTORY.md), a fully working version was [coded in C in 2002](https://github.com/squillero/microgp2) and then [re-engineered in C++ in 2006](https://github.com/squillero/microgp3). 

This version is in Python, it has been redesigned from scratch once again to take advantage of the peculiar features of the language and to exploit its huge standard library. It would not have been possible without the help and support of [several people](CONTRIBUTORS.md). 

**Copyright © 2020 Giovanni Squillero and Alberto Tonda**  
MicroGP v4 is [free and open-source software](https://en.wikipedia.org/wiki/Free_and_open-source_software), and it is distributed under the permissive [Apache-2.0 license](https://www.tldrlegal.com/l/apache2).