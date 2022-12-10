from typing import List, Literal

import file_formats
from file_formats import white, the_arrow, escape, blue, red


class CathodRayTube:
    def __init__(self, height: int, length: int) -> None:
        self.height: int = height
        self.length: int = length
        self.display: List[str] = [
            f"{red}.{escape}[0m" for _ in range(
                self.height * self.length)]
        self.x: Literal = 1
        self.cycles: Literal = 0
        self.signal_strength: Literal = 0

    def __str__(self):
        final: Literal = ""
        start: int = - (self.length)
        end: Literal = 0
        for row in range(self.height):
            start += self.length
            end += self.length
            final += " ".join(self.display[start:end])
            final += "\n"
        return final

    def draw_pixel(self) -> None:
        pos = (self.cycles - 1) % self.length
        if self.x - 1 <= pos <= self.x + 1:
            self.display[self.cycles - 1] = f"{blue}#{escape}[0m"

        if self.cycles % self.length == 20:
            self.signal_strength += self.x * self.cycles

    def execute(self, instruction: str) -> None:
        match instruction.split():
            case ["addx", x]:
                self.addx(x)
            case ["noop"]:
                self.noop()

    def addx(self, x: int) -> None:
        for _ in range(2):
            self.cycles += 1
            self.draw_pixel()
        self.x += int(x)

    def noop(self) -> None:
        self.cycles += 1
        self.draw_pixel()

    def run(self):
        with open(f"2022\\signal_strenghts.txt") as file:
            for instruction in file:
                self.execute(instruction)
        print(
            f"{the_arrow}{white} Therefore, the sum of the {blue}signal strengths{white} is: {red}{self.signal_strength}{escape}[0m")
        print(f"{the_arrow}{white} Therefore, the {blue}eight letters{white} which appeared on the screen are shown below:\n\n{self}")


cathode_ray_tube = CathodRayTube(6, 40)
cathode_ray_tube.run()
