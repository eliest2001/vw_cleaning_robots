from dataclasses import dataclass
from src.domain.value_objects.direction import Direction
from src.domain.value_objects.position import Position


@dataclass
class Robot:
    id: str
    position: Position
    direction: Direction
    
    def move_forward(self):
        self.position = self.position.next(self.direction)
    
    def rotate_left(self):
        self.direction = self.direction.left()
    
    def rotate_right(self):
        self.direction = self.direction.right()