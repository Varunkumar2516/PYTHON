# FORMAT CODES In Python

| Format Code | Meaning                                    | Example Output             |
| ----------- | ------------------------------------------ | -------------------------- |
| `%a`        | Abbreviated weekday name                   | `Mon`                      |
| `%A`        | Full weekday name                          | `Monday`                   |
| `%w`        | Weekday as a decimal (0 = Sunday)          | `1`                        |
| `%d`        | Day of the month (zero-padded)             | `05`                       |
| `%b`        | Abbreviated month name                     | `Jul`                      |
| `%B`        | Full month name                            | `July`                     |
| `%m`        | Month as a decimal number (01–12)          | `07`                       |
| `%y`        | Year without century (00–99)               | `25`                       |
| `%Y`        | Year with century                          | `2025`                     |
| `%H`        | Hour (24-hour clock, 00–23)                | `14`                       |
| `%I`        | Hour (12-hour clock, 01–12)                | `02`                       |
| `%p`        | AM/PM                                      | `PM`                       |
| `%M`        | Minute (00–59)                             | `30`                       |
| `%S`        | Second (00–59)                             | `08`                       |
| `%f`        | Microsecond (000000–999999)                | `548513`                   |
| `%z`        | UTC offset                                 | `+0530`                    |
| `%Z`        | Time zone name                             | `IST`                      |
| `%j`        | Day of year (001–366)                      | `193`                      |
| `%U`        | Week number (Sunday as first day)          | `27`                       |
| `%W`        | Week number (Monday as first day)          | `27`                       |
| `%c`        | Locale’s date and time                     | `Sat Jul 12 14:30:00 2025` |
| `%x`        | Locale’s date                              | `07/12/25`                 |
| `%X`        | Locale’s time                              | `14:30:00`                 |
| `%%`        | Literal `%` character                      | `%`                        |
| `%C`        | Century (year divided by 100, zero-padded) | `20`                       |
| `%u`        | ISO weekday (1=Monday, 7=Sunday)           | `6`                        |
| `%V`        | ISO week number (01–53)                    | `28`                       |
| `%G`        | ISO 8601 year                              | `2025`                     |



__ These codes work with:

datetime.strftime() and datetime.strptime()

time.strftime() and time.strptime()__