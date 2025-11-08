# Programming Bootcamp

**By Stephen Singer**

## Introduction

This repository contains original learning materials, hands-on exercises, and code snippets for a **Python Programming
Fundamentals** course.

It is structured for **complete beginners**, but can also serve as a **crash course for experienced developers** who
want to get up to speed with Python. The program covers core syntax, control structures, data structures, and
object-oriented design. It then branches into intermediate topics like file input and output, basic app development, and
web
fundamentals.

Learning to program is not always easy. But the ability to break down problems, write logical solutions, and build
working software is one of the most rewarding and empowering skills you can develop today. This course was designed to
help you get there with structure, practice, and a bit of fun along the way.

By the end of the course, you should be able to:

- Read, write, and debug non-trivial Python programs
- Solve beginner to intermediate programming problems
- Build and understand small-scale software projects
- Decide which specific path in tech you'd like to pursue next

**Suggested flow:**

1. Read through the slides
2. Run and experiment with the sample code
3. Attempt the exercises
4. Review the labs or projects to apply what you've learned
5. Check your solution with the given solution and look for improvements

## Pacing

The material is designed for a **4-day bootcamp**:

- **9 hours/day**, with short breaks and longer lab periods
- Ideal for fast learners or those with prior coding experience

For absolute beginners, a **2-week pace** is recommended:

- **4 hours/day**, 5 days a week
- Allows for deeper review, repetition, and exploration

You can also opt for a **4-week pace**

- **2 hours/day**, 5 days a week
- Maximize retention and reinforces habit with much less stress

For a busy schedule, you can also opt for **16-weeks** (university pacing)

- **3 hours/week**, either in a single day or divided across days
- Easier maintenance but might hurt retention if schedule is inconsistent

> You can also do both: finish the bootcamp at full speed, then revisit everything slowly with real-world projects.

## Course Outline

Each day contains slide decks, code samples, hands-on exercises, and lab activities.

| Day       | Topics                                                                     |
|-----------|----------------------------------------------------------------------------|
| **Day 1** | Introduction, input/output, variables, control flow, functions             |
| **Day 2** | Lists, tuples, dictionaries, sets, comprehension, strings, file handling   |
| **Day 3** | Classes, object-oriented programming principles, GUI programming (tkinter) |
| **Day 4** | Modules, libraries, best practices, web development introduction           |

## Getting Started

### Install Python

- [Download Python](https://www.python.org/downloads/)
    - ☑️ Enable "Add Python to PATH"
    - ☑️ Enable "Use admin privileges when installing py.exe"

### Install an Editor (Recommended: PyCharm)

- [Download PyCharm](https://www.jetbrains.com/pycharm/download/)
    - While any editor works (VS Code, Sublime, etc.), all examples here are aligned with PyCharm for consistency.

### Console Essentials (Optional)

### Running Python

If you're not using PyCharm, you can run any `.py` file with:

```bash
python filename.py
```

On macOS/Linux, use:

```bash
python3 filename.py
```

To open an interactive shell:

```bash
python
# or
python3
```

### Package Management

To avoid version conflicts, create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate     # macOS/Linux
venv\Scripts\activate        # Windows
```

Then install packages as needed:

```bash
pip install flask
```

### Clone the Repository

1. Sign up at [GitHub](https://github.com) and fork this repository.
2. In PyCharm:
    - Click **"Get from Version Control"**
    - Paste your fork URL
    - Log in with your GitHub account if prompted
3. When asked to configure interpreter:
    - Add a **local Python interpreter** via "Add Python Interpreter" → OK

> A visual guide is available in
> the [Day 1 Slides](https://github.com/Ayumu098/python-bootcamp/blob/master/slides/Day%2001%20-%20Introduction%20to%20Python%20and%20Basic%20Syntax.pdf)

Alternatively, if you're comfortable with Git:

```bash
git clone https://github.com/Ayumu098/python-bootcamp.git
```

Then open the folder in your preferred editor.

### Google Collab

If you don’t want to install Python right away, you can use Google Colab. It's like Google Docs, but for Python code.

- Go to [colab.research.google.com](colab.research.google.com)
- Click "New Notebook"
- You can write and run Python directly in your browser (no setup required)

It’s great for experimenting and practicing, but keep in mind:

- Files don’t persist locally unless you download them or connect Colab to your Google Drive.
- Some libraries may not be preinstalled. You can add them with `!pip install library-name`
- GUI apps (like tkinter) won’t work. Colab is best for console-based code, data science, and quick prototypes.

## Prerequisites

- Basic computer skills (navigating folders, installing software)
- Curiosity, patience, and a willingness to learn by doing

## External Materials & Further Reading

### Python Fundamentals

- [Python Official Docs](https://docs.python.org/3/)
- [W3Schools Python Tutorial](https://www.w3schools.com/python/)
- [Real Python](https://realpython.com/)
- [Python Tutor (Code Visualizer)](https://pythontutor.com/)

### Recommended Books

- *Automate the Boring Stuff with Python* – Al Sweigart
- *Python Crash Course* – Eric Matthes
- *Fluent Python* – Luciano Ramalho

### Recommended Channels

- [Visually Explained](https://www.youtube.com/@VisuallyExplainedEducation/videos)
- [Bro Code](https://www.youtube.com/watch?v=XKHEtdqhLK8&t=3497s)
- [SDPT Solutions](https://www.youtube.com/watch?v=UBZs0-gUZsU&list=PLVnJhHoKgEmpbmB-Lrb2m4wwq5IPgLHnG)

### Interactive Practice

- [Exercism Python Track](https://exercism.org/tracks/python)
- [HackerRank Easy Problems](https://www.hackerrank.com/domains/python?filters%5Bdifficulty%5D%5B%5D=easy)
- [LeetCode Beginner Problems](https://leetcode.com/problemset/all/?difficulty=Easy)

## What's Next

After completing this bootcamp, try:

- A [100 Days of Code](https://www.100daysofcode.com/) challenge
- Building a personal project (blog, tracker, automation tool)
- Contributing to a
  beginner-friendly [open-source project](https://github.com/search?q=label%3Agood-first-issue&type=issues)
- Exploring specializations: data science, web dev, game dev, automation

### Bonus Content

See the bonus folder for:

- Functional programming
- OpenPyXL (Excel automation)
- Pandas (data science)
- Streamlit (simple web apps)
- BeautifulSoup (web scraping)

These aren't covered in-depth during the bootcamp, but they are excellent warmups.

### Sample Projects to Explore

These beginner/intermediate projects are great for practice:

- [Pygame Tutorial](https://github.com/techwithtim/Pygame-Tutorials)
- [Tkinter Collection](https://github.com/Aashishkumar123/Python-GUI-Project)
- [Flask Blog App](https://github.com/CoreyMSchafer/code_snippets/tree/master/Python/Flask_Blog)
- [Other Mini Projects](https://github.com/Python-World/python-mini-projects)

### Packaging Python Applications

Packaging Python as Executables / Apps

You can ship Python programs as .exe (Windows) or runnable apps (Mac/Linux) so users don’t need Python installed.

#### PyInstaller

```bash
pip install pyinstaller
pyinstaller --onefile your_script.py
```

- Output: `dist/your_script.exe` (or binary).
- Docs: [PyInstaller Manual](https://pyinstaller.org/en/stable/?utm_source=chatgpt.com)

#### cx_Freeze

```bash
pip install cx_Freeze
cxfreeze your_script.py --target-dir dist/
```

- Output: folder with executable.
- Docs: [cx_Freeze Docs](https://cx-freeze.readthedocs.io/en/stable/?utm_source=chatgpt.com)

#### py2exe (Windows-only)

```bash
pip install py2exe
python setup.py py2exe
```

Requires a `setup.py` script.

Docs: [py2exe Guide](https://www.py2exe.org/?utm_source=chatgpt.com)

## Feedback & Issues

If you encounter any bugs or have suggestions for improvement, feel free
to [open an issue](https://github.com/Ayumu098/python-bootcamp/issues).

Forking and adapting this repo for your own training sessions or learning goals is encouraged.

> If you have any questions or further inquiries, you can email me at stephen.singer@gmail.com

## FAQs

### Do I need to pay for Python or PyCharm?

No. Python is free and open-source. PyCharm is free Community Edition which is all you need for this course.

### Will this be enough to get a programming job?

This bootcamp is a launchpad, not the destination. You'll walk away with a solid foundation and the confidence to read,
write, and debug Python programs. However, being job-ready usually takes more practice, more projects, and deeper
specialization (like web development, data science, or automation). Fully appreciate the fundamentals so that any
advanced topic is easier to approach.

> Think of this as learning to ride a bike. You won’t be racing yet, but you’ll know how to balance, steer, and pedal.

### What if I get stuck or don’t understand something?

Great. That means there's more to learn. Programming is 50% getting stuck. Not even senior developers can code without
errors or completely understand code. Like any technical skill, it requires careful steps and practice until it becomes
familiar.

> Walk away from the keyboard. Eat a snack, take a nap, or do something else. Problems often solve themselves when you
> come back with a fresh brain. Another good thing to do if you're stuck is to explain the problem to a friend. They can
> give fresh insights and your effort to explain can sometimes reveal logical gaps you may have missed.

Ask questions during the session, Google a lot, and use the repo’s issues page or email if you need extra help.

Here are some techniques to help debug code:

1. **Show Everything:** Add `print()` or log statements to check what your variables look like at each step.
2. **Go Step by Step:** Don’t try to debug the whole program at once. Isolate the smallest piece that's broken.
3. **Use a Debugger:** Tools like PyCharm’s debugger or pdb let you pause code and inspect it line by line.
4. **Reproduce the Bug:** If you can make the error happen consistently, you’re halfway to fixing it.

### How do I improve faster?

1. **Practice Smart:** Solve problems, then check solutions once finished, or after you hit a wall. Looking at the
   solution isn't cheating. it’s learning. The goal is to bridge the gap between what you tried and how it could be done
   better. This leads to the next point.

2. **Spot Patterns:** Most problems you face are just remixes of old problems. Learn common patterns (loops, conditions,
   recursion, searching, sorting) and you’ll start seeing them everywhere. This is where formal books and forums come in
   handy.

3. **Build Experience:** At first, coding feels like crawling through mud. But every problem you solve makes the next
   one faster. One day you look back and realize something that used to take you hours now takes minutes.

### What are some tips when approaching problems

1. **Scope the Problem:** Figure out what’s actually being asked. Ignore fluff. Focus on inputs, outputs, and what the
   code needs to do.
2. **Think Like a Human:** Solve it by hand first, step by step, before touching code.
3. **List Unknowns:** Write down everything you don’t understand, then research one by one. If you hit a wall, ask for
   help.
4. **Make it Work First:** Pretty code comes later. Get any working solution first, then refactor for readability or
   efficiency.
5. **Use Libraries:** Don’t reinvent the wheel. If Python already has a function for it, use it.

### Is there homework?

No mandatory homework. Instead, you’re encouraged to revisit your own code and make it better. Try the harder labs if
you want a challenge, or tweak your previous solutions to be cleaner and more efficient.

## Final Note

This bootcamp is a **starting point** — not a finish line. The goal is to build a strong mental model of how code works,
and to practice applying it until it becomes second nature.

Learning to code is tough. It’s frustrating, messy, and non-linear. But it’s also one of the most valuable, empowering
skills you can build — not just for your career, but for your confidence.

If you make it through, even once, you're already ahead of most people.

Good luck and happy coding

## License

This project is licensed under the [MIT License](LICENSE).  
Feel free to fork, modify, and use it for your own learning or teaching.
