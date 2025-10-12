# Project PROPOSAL for Loris Bertschi's Project

## Project Title & Category

### 1. Project Title

"Portfolio Insight: An Integrated Reporting Tool for Multi-Account Investors"

### 2. Project category

My project is likely to fall in the Data Analysis & Visualization category as it involve generating reports coupled with analysing some data and deriving KPI's from it. 

## Problem Statement & Motivation

Investing in the financial markets is already complex, but tracking and understanding your own performance adds another layer of difficulty. As a personal investor, and someone constantly surrounded by others who actively trade, I often hear the same frustration from my peers, beyond buying high and selling low, the biggest challenge is accurately assessing their real gains and losses.

Most online trading platforms include a built-in performance tracker or P/L tool that’s precise, well-designed, and updates instantly. However, no single app offers access to every type of asset or security an investor might want. As a result, many investors end up juggling multiple trading apps, managing several accounts, and tracking different portfolios across various platforms. This fragmentation makes it difficult to get a clear, consolidated picture of overall performance.

The goal of this project is to build an application or interface that allows users to centralize all their holdings and investments in one place. By entering their positions and relevant details, users will be able to monitor their total portfolio performance and receive daily or weekly reports offering a clear, visual overview of their returns across all platforms and asset class. 


1. Go to GitHub Classroom
2. Click "New assignment"
3. Configure as follows:

**Basic Information:**
- Title: "Problem Set 3: Git & Python Fundamentals"
- Deadline: (Optional - leave blank for ungraded)
- Individual assignment

**Starter Code:**
- Repository template: Select your `ps3-template` repository
- Repository visibility: Private

**Autograding Tests:**

Add these tests in GitHub Classroom:

| Test Name | Setup Command | Run Command | Points |
|-----------|--------------|-------------|---------|
| Check Git Log | - | test -f git_log.txt | 0 |
| Test Temperature Converter | pip install pytest | pytest test_assignment.py::test_celsius_to_fahrenheit test_assignment.py::test_fahrenheit_to_celsius -v | 0 |
| Test Number Analysis | pip install pytest | pytest test_assignment.py::test_analyze_numbers -v | 0 |
| Test File Operations | pip install pytest | pytest test_assignment.py::test_file_operations -v | 0 |

**Note:** Points are set to 0 since this is ungraded. You can add points if you decide to grade it.

### 3. Enable GitHub Actions

Make sure GitHub Actions is enabled in your organization settings for autograding to work.

### 4. Get Assignment Link

After creating the assignment, GitHub Classroom will provide a link like:
`https://classroom.github.com/a/XXXXXXX`

Update this link in the course materials.

## Files in This Template

### Student Files (To Complete)
- `problem2.py` - Temperature converter (skeleton provided)
- `problem3.py` - Number analysis (skeleton provided)
- `problem4.py` - File word counter (skeleton provided)
- `bonus_password_generator.py` - Optional bonus (skeleton provided)

### Testing Files
- `test_assignment.py` - Automated tests for grading
- `requirements.txt` - Python dependencies (pytest)
- `.github/workflows/classroom.yml` - GitHub Actions workflow

### Documentation
- `README.md` - Student instructions
- `.gitignore` - Git ignore file

## Customization Options

### To Make It Graded:
1. Add points to each test in GitHub Classroom
2. Add a due date
3. Update the assignment description to mention grading

### To Add More Tests:
1. Edit `test_assignment.py` to add more test functions
2. Add corresponding test configurations in GitHub Classroom

### To Change Difficulty:
- **Easier:** Provide more code in the skeleton files
- **Harder:** Remove helper comments and function signatures

## Student Workflow

1. Students accept the assignment via the GitHub Classroom link
2. Clone their personal repository
3. Complete the problems
4. Commit and push their solutions
5. GitHub Actions runs tests automatically
6. Students can see test results in the Actions tab

## Common Issues

### Tests Not Running
- Check that GitHub Actions is enabled
- Verify the workflow file is in `.github/workflows/`
- Check Python version compatibility

### Import Errors
- Make sure all problem files are in the root directory
- Check that function names match exactly

### Git Log Missing
- Students need to run `git log --oneline > git_log.txt` after making commits

## Support

For issues with:
- GitHub Classroom: Check GitHub Education documentation
- Test failures: Review `test_assignment.py` for requirements
- Python issues: Ensure Python 3.8+ is being used