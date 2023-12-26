
```markdown
# FUZZing Tool

## Description
This is a simple FUZZing tool written in Python using the `requests` library and `ThreadPoolExecutor`. The tool is designed to perform fuzz testing on a specified URL using a wordlist, allowing users to check for different endpoints and their corresponding status codes.

## Usage
### Prerequisites
- Python 3.x
- `requests` library

### Command Line Arguments
- `-u` or `--url`: Specify the target URL.
- `-fc` or `--filter_code`: Filter output with a list of status codes (optional).
- `-mc` or `--matching_code`: Match output with a list of status codes (optional).
- `-w` or `--wordlist`: Specify the path to the Wordlist file.

```
### Example
```bash
python fuzzing_tool.py -u http://example.com -fc 500,502 -w wordlist.txt
```
## Script Details
The script performs fuzz testing by making HEAD requests to different endpoints formed by appending words from the provided wordlist to the base URL. It utilizes a ThreadPoolExecutor for concurrent requests to improve efficiency.

## Output
The script will display the status codes of the tested endpoints. Optionally, you can filter or match the output based on status codes.

## Notes
- If using a large wordlist, consider using filters to narrow down the results.
- Be mindful of the target's security policies and ensure testing is performed responsibly.

