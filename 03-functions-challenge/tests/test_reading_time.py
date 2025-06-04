import pytest
from lib.reading_time import *

def test_empty_string_gives_time_zero():
    result = reading_time_in_minutes("")
    assert result == 0

def test_string_with_less_than_100_words():
    result = reading_time_in_minutes("short sentence test")
    assert result == 0

def test_string_with_200_words():
    result = reading_time_in_minutes(text)
    assert result == 1

def test_longer_string_with_1000_words():
    result = reading_time_in_minutes(long_text)
    assert result == 5

def test_none_value_returns_error():
    with pytest.raises(Exception) as e:
        reading_time_in_minutes(None)
    message = str(e.value)
    assert message == "Enter a string input"

# text = " ".join(["word" for i in range(0, 200)])

text = """"
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent placerat sem sed turpis eleifend, in dapibus velit egestas. 
Praesent rhoncus, metus ac elementum ultricies, dui augue volutpat felis, vehicula sodales nunc turpis a lectus. Nunc commodo, 
nulla a feugiat convallis, augue ligula lacinia neque, eu euismod mauris purus vel diam. Donec placerat nulla at tortor malesuada, 
varius pellentesque nisl faucibus. In sit amet tortor non dui interdum semper vel rutrum orci. Maecenas euismod sem in odio lobortis, 
quis ullamcorper velit posuere. Praesent dapibus faucibus lorem maximus tempor. Nunc imperdiet orci sed quam vulputate congue ut sed metus.

Quisque purus odio, congue nec nulla lobortis, condimentum egestas est. Etiam elit turpis, condimentum at fermentum vel, consectetur id diam. 
Nulla imperdiet convallis arcu vel luctus. Curabitur in libero eget justo accumsan blandit. Vivamus id vulputate arcu, vel venenatis magna. 
Aliquam in massa justo. Suspendisse pulvinar auctor augue. Nunc nisl justo, sodales placerat tellus id, condimentum euismod felis. Nam tincidunt 
congue ex eget facilisis. Nullam nisl neque, fermentum eu turpis ut, aliquam efficitur sapien. Maecenas vestibulum nec sapien in dictum. 
Phasellus non orci vel magna molestie consequat et id tellus. Nunc faucibus massa eu maximus pellentesque. Aliquam turpis nisl, placerat ut risus eget.
"""

long_text = """"
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent placerat sem sed turpis eleifend, in dapibus velit egestas. 
Praesent rhoncus, metus ac elementum ultricies, dui augue volutpat felis, vehicula sodales nunc turpis a lectus. Nunc commodo, 
nulla a feugiat convallis, augue ligula lacinia neque, eu euismod mauris purus vel diam. Donec placerat nulla at tortor malesuada, 
varius pellentesque nisl faucibus. In sit amet tortor non dui interdum semper vel rutrum orci. Maecenas euismod sem in odio lobortis, 
quis ullamcorper velit posuere. Praesent dapibus faucibus lorem maximus tempor. Nunc imperdiet orci sed quam vulputate congue ut sed metus.

Quisque purus odio, congue nec nulla lobortis, condimentum egestas est. Etiam elit turpis, condimentum at fermentum vel, consectetur id diam. 
Nulla imperdiet convallis arcu vel luctus. Curabitur in libero eget justo accumsan blandit. Vivamus id vulputate arcu, vel venenatis magna. 
Aliquam in massa justo. Suspendisse pulvinar auctor augue. Nunc nisl justo, sodales placerat tellus id, condimentum euismod felis. Nam tincidunt 
congue ex eget facilisis. Nullam nisl neque, fermentum eu turpis ut, aliquam efficitur sapien. Maecenas vestibulum nec sapien in dictum. 
Phasellus non orci vel magna molestie consequat et id tellus. Nunc faucibus massa eu maximus pellentesque. Aliquam turpis nisl, placerat ut risus eget.

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent placerat sem sed turpis eleifend, in dapibus velit egestas. 
Praesent rhoncus, metus ac elementum ultricies, dui augue volutpat felis, vehicula sodales nunc turpis a lectus. Nunc commodo, 
nulla a feugiat convallis, augue ligula lacinia neque, eu euismod mauris purus vel diam. Donec placerat nulla at tortor malesuada, 
varius pellentesque nisl faucibus. In sit amet tortor non dui interdum semper vel rutrum orci. Maecenas euismod sem in odio lobortis, 
quis ullamcorper velit posuere. Praesent dapibus faucibus lorem maximus tempor. Nunc imperdiet orci sed quam vulputate congue ut sed metus.

Quisque purus odio, congue nec nulla lobortis, condimentum egestas est. Etiam elit turpis, condimentum at fermentum vel, consectetur id diam. 
Nulla imperdiet convallis arcu vel luctus. Curabitur in libero eget justo accumsan blandit. Vivamus id vulputate arcu, vel venenatis magna. 
Aliquam in massa justo. Suspendisse pulvinar auctor augue. Nunc nisl justo, sodales placerat tellus id, condimentum euismod felis. Nam tincidunt 
congue ex eget facilisis. Nullam nisl neque, fermentum eu turpis ut, aliquam efficitur sapien. Maecenas vestibulum nec sapien in dictum. 
Phasellus non orci vel magna molestie consequat et id tellus. Nunc faucibus massa eu maximus pellentesque. Aliquam turpis nisl, placerat ut risus eget.

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent placerat sem sed turpis eleifend, in dapibus velit egestas. 
Praesent rhoncus, metus ac elementum ultricies, dui augue volutpat felis, vehicula sodales nunc turpis a lectus. Nunc commodo, 
nulla a feugiat convallis, augue ligula lacinia neque, eu euismod mauris purus vel diam. Donec placerat nulla at tortor malesuada, 
varius pellentesque nisl faucibus. In sit amet tortor non dui interdum semper vel rutrum orci. Maecenas euismod sem in odio lobortis, 
quis ullamcorper velit posuere. Praesent dapibus faucibus lorem maximus tempor. Nunc imperdiet orci sed quam vulputate congue ut sed metus.

Quisque purus odio, congue nec nulla lobortis, condimentum egestas est. Etiam elit turpis, condimentum at fermentum vel, consectetur id diam. 
Nulla imperdiet convallis arcu vel luctus. Curabitur in libero eget justo accumsan blandit. Vivamus id vulputate arcu, vel venenatis magna. 
Aliquam in massa justo. Suspendisse pulvinar auctor augue. Nunc nisl justo, sodales placerat tellus id, condimentum euismod felis. Nam tincidunt 
congue ex eget facilisis. Nullam nisl neque, fermentum eu turpis ut, aliquam efficitur sapien. Maecenas vestibulum nec sapien in dictum. 
Phasellus non orci vel magna molestie consequat et id tellus. Nunc faucibus massa eu maximus pellentesque. Aliquam turpis nisl, placerat ut risus eget.

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent placerat sem sed turpis eleifend, in dapibus velit egestas. 
Praesent rhoncus, metus ac elementum ultricies, dui augue volutpat felis, vehicula sodales nunc turpis a lectus. Nunc commodo, 
nulla a feugiat convallis, augue ligula lacinia neque, eu euismod mauris purus vel diam. Donec placerat nulla at tortor malesuada, 
varius pellentesque nisl faucibus. In sit amet tortor non dui interdum semper vel rutrum orci. Maecenas euismod sem in odio lobortis, 
quis ullamcorper velit posuere. Praesent dapibus faucibus lorem maximus tempor. Nunc imperdiet orci sed quam vulputate congue ut sed metus.

Quisque purus odio, congue nec nulla lobortis, condimentum egestas est. Etiam elit turpis, condimentum at fermentum vel, consectetur id diam. 
Nulla imperdiet convallis arcu vel luctus. Curabitur in libero eget justo accumsan blandit. Vivamus id vulputate arcu, vel venenatis magna. 
Aliquam in massa justo. Suspendisse pulvinar auctor augue. Nunc nisl justo, sodales placerat tellus id, condimentum euismod felis. Nam tincidunt 
congue ex eget facilisis. Nullam nisl neque, fermentum eu turpis ut, aliquam efficitur sapien. Maecenas vestibulum nec sapien in dictum. 
Phasellus non orci vel magna molestie consequat et id tellus. Nunc faucibus massa eu maximus pellentesque. Aliquam turpis nisl, placerat ut risus eget.

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent placerat sem sed turpis eleifend, in dapibus velit egestas. 
Praesent rhoncus, metus ac elementum ultricies, dui augue volutpat felis, vehicula sodales nunc turpis a lectus. Nunc commodo, 
nulla a feugiat convallis, augue ligula lacinia neque, eu euismod mauris purus vel diam. Donec placerat nulla at tortor malesuada, 
varius pellentesque nisl faucibus. In sit amet tortor non dui interdum semper vel rutrum orci. Maecenas euismod sem in odio lobortis, 
quis ullamcorper velit posuere. Praesent dapibus faucibus lorem maximus tempor. Nunc imperdiet orci sed quam vulputate congue ut sed metus.

Quisque purus odio, congue nec nulla lobortis, condimentum egestas est. Etiam elit turpis, condimentum at fermentum vel, consectetur id diam. 
Nulla imperdiet convallis arcu vel luctus. Curabitur in libero eget justo accumsan blandit. Vivamus id vulputate arcu, vel venenatis magna. 
Aliquam in massa justo. Suspendisse pulvinar auctor augue. Nunc nisl justo, sodales placerat tellus id, condimentum euismod felis. Nam tincidunt 
congue ex eget facilisis. Nullam nisl neque, fermentum eu turpis ut, aliquam efficitur sapien. Maecenas vestibulum nec sapien in dictum. 
Phasellus non orci vel magna molestie consequat et id tellus. Nunc faucibus massa eu maximus pellentesque. Aliquam turpis nisl, placerat ut risus eget.
"""
