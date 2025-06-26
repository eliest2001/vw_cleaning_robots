from dataclasses import dataclass, field
from uuid import uuid4
from src.domain.value_objects.direction import Direction
from src.domain.value_objects.position import Position


@dataclass
class Robot:
    position: Position
    direction: Direction
    id: str = field(default_factory=lambda: str(uuid4()))
    
    def move_forward(self):
        self.position = self.position.next(self.direction)
    
    def rotate_left(self):
        self.direction = self.direction.left()
    
    def rotate_right(self):
        self.direction = self.direction.right()
        
    def format(self, length: int):
        x_str = str(self.position.x).zfill(length)
        y_str = str(self.position.y).zfill(length)
        return f"{x_str}{y_str} {self.direction}"