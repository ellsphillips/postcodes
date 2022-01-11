# <img height=30 src="https://latex.codecogs.com/svg.latex?{\textsf{\bfseries\color[RGB]{255,216,102}postcodes}}" alt="postcodes"> <img align="right" height="100" title="Doctor" src="https://user-images.githubusercontent.com/27974647/148956116-b75f6a9b-b518-42d1-b42a-0b8e0de904ef.png">

`postcodes` is a simple API for UK-based postcodes, covering codes with 5 to 7 alphanumeric characters with option to extend to islands and London boroughs.

# Structure

<img width="100%" title="Postcode structure" src="https://www.getthedata.com/images/postcode_format.png">

<br>

# Example

<center>

| Example: np108xg   |          |
| ------------------ | -------- |
| Valid?             | Yes      |
| Formatted Postcode | NP10 8XG |
| Outward Code       | NP10     |
| Inward Code        | 8XG      |
| Postcode Area      | NP       |
| District Code      | NP1      |
| Sub-District       | N/A      |
| Sector             | NP10 8   |
| Unit               | XG       |

</center>

# Usage

```python
  from postcodes import Postcode

  postcode = Postcode("NP10 8XG")

  print(postcode.is_valid)
  # True

  print(
      json.dumps(postcode.components, indent=4)
  )
  # {
  #     "COMPLETE": "NP10 8XG",
  #     "OUTWARD": "NP10",
  #     "AREA": "NP",
  #     "DISTRICT": "10",
  #     "SUBDISTRICT": "N/A",
  #     "INWARD": "8XG",
  #     "SECTOR": "8",
  #     "UNIT": "XG"
  # }
```
