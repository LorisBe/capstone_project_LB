# GitHub Classroom Setup Guide for Week 3

## Setting Up the Assignment in GitHub Classroom

### 1. Create Template Repository

1. Create a new repository on GitHub called `ps3-template`
2. Upload all files from this directory to the template repository
3. Go to Settings → Template repository → Check "Template repository"

### 2. Create GitHub Classroom Assignment

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