from langchain_core.tools import tool
from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper
from word2number import w2n

def safe_parse_number(val) -> float:
    """Helper function to parse either raw digits, floats, or word formats safely."""
    # If it's already a number, convert to float directly
    if isinstance(val, (int, float)):
        return float(val)
    
    clean_val = str(val).strip().lower()
    try:
        # Try evaluating as a raw numeric digit or float first (e.g., "20" or "20.5")
        return float(clean_val)
    except ValueError:
        try:
            # Fallback to word string parsing (e.g., "twenty" -> 20.0)
            return float(w2n.word_to_num(clean_val))
        except ValueError:
            raise ValueError(f"Could not convert text '{val}' into a valid number.")

# --- Mathematical Operators ---

@tool
def addition(a: str, b: str) -> str:
    """Performs addition on two inputs. Accepts numbers (e.g., '20') or word text (e.g., 'twenty')."""
    try:
        num_a = safe_parse_number(a)
        num_b = safe_parse_number(b)
        return str(num_a + num_b)
    except Exception as e:
        return f"Error parsing arguments: {str(e)}"

@tool
def subtraction(a: str, b: str) -> str:
    """Performs subtraction on two inputs. Accepts numbers (e.g., '20') or word text (e.g., 'twenty')."""
    try:
        num_a = safe_parse_number(a)
        num_b = safe_parse_number(b)
        return str(num_a - num_b)
    except Exception as e:
        return f"Error parsing arguments: {str(e)}"

@tool
def multiply(a: str, b: str) -> str:
    """Performs multiplication on two inputs. Accepts numbers (e.g., '20') or word text (e.g., 'twenty')."""
    try:
        num_a = safe_parse_number(a)
        num_b = safe_parse_number(b)
        return str(num_a * num_b)
    except Exception as e:
        return f"Error parsing arguments: {str(e)}"

@tool
def division(a: str, b: str) -> str:
    """Performs division on two inputs. Accepts numbers (e.g., '20') or word text (e.g., 'twenty')."""
    try:
        num_a = safe_parse_number(a)
        num_b = safe_parse_number(b)
        if num_b == 0:
            return "Error: Division by zero is not allowed."
        return str(num_a / num_b)
    except Exception as e:
        return f"Error parsing arguments: {str(e)}"

# --- Wikipedia Lookup ---
wiki_wrapper = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=1000)
wikipedia_tool = WikipediaQueryRun(api_wrapper=wiki_wrapper)

# Export tools
tool_kit = [addition, subtraction, multiply, division, wikipedia_tool]
