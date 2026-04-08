import pygame
import random

# 화면 설정
SCREEN_WIDTH = 300
SCREEN_HEIGHT = 600
BLOCK_SIZE = 30

# 색상
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
COLORS = [
    (0, 255, 255),  # I
    (0, 0, 255),    # J
    (255, 165, 0),  # L
    (255, 255, 0),  # O
    (0, 255, 0),    # S
    (128, 0, 128),  # T
    (255, 0, 0)     # Z
]

# 블록 모양
SHAPES = [
    [[1, 1, 1, 1]],       # I
    [[1, 0, 0], [1, 1, 1]], # J
    [[0, 0, 1], [1, 1, 1]], # L
    [[1, 1], [1, 1]],      # O
    [[0, 1, 1], [1, 1, 0]], # S
    [[0, 1, 0], [1, 1, 1]], # T
    [[1, 1, 0], [0, 1, 1]]  # Z
]

class Tetris:
    def __init__(self):
        self.width = SCREEN_WIDTH // BLOCK_SIZE
        self.height = SCREEN_HEIGHT // BLOCK_SIZE
        self.board = [[0]*self.width for _ in range(self.height)]
        self.game_over = False
        self.current_piece = self.get_new_piece()
        self.x = self.width // 2 - len(self.current_piece['shape'][0]) // 2
        self.y = 0
        self.score = 0

    def get_new_piece(self):
        shape = random.choice(SHAPES)
        color = COLORS[SHAPES.index(shape)]
        return {'shape': shape, 'color': color}

    def rotate(self):
        self.current_piece['shape'] = [list(row) for row in zip(*self.current_piece['shape'][::-1])]
        if self.collision(self.x, self.y):
            self.current_piece['shape'] = [list(row) for row in zip(*self.current_piece['shape'])][::-1]

    def collision(self, x_offset, y_offset):
        shape = self.current_piece['shape']
        for y, row in enumerate(shape):
            for x, cell in enumerate(row):
                if cell:
                    if (x + x_offset < 0 or x + x_offset >= self.width or
                        y + y_offset >= self.height or
                        self.board[y + y_offset][x + x_offset]):
                        return True
        return False

    def freeze(self):
        shape = self.current_piece['shape']
        color = self.current_piece['color']
        for y, row in enumerate(shape):
            for x, cell in enumerate(row):
                if cell:
                    self.board[self.y + y][self.x + x] = color
        self.clear_lines()
        self.current_piece = self.get_new_piece()
        self.x = self.width // 2 - len(self.current_piece['shape'][0]) // 2
        self.y = 0
        if self.collision(self.x, self.y):
            self.game_over = True

    def clear_lines(self):
        new_board = [row for row in self.board if any(cell == 0 for cell in row)]
        lines_cleared = self.height - len(new_board)
        self.score += lines_cleared * 10
        self.board = [[0]*self.width for _ in range(lines_cleared)] + new_board

    def move(self, dx):
        if not self.collision(self.x + dx, self.y):
            self.x += dx

    def drop(self):
        if not self.collision(self.x, self.y + 1):
            self.y += 1
        else:
            self.freeze()

def draw_board(screen, game):
    screen.fill(BLACK)
    # 고정 블록
    for y, row in enumerate(game.board):
        for x, cell in enumerate(row):
            if cell:
                pygame.draw.rect(screen, cell, (x*BLOCK_SIZE, y*BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
                pygame.draw.rect(screen, WHITE, (x*BLOCK_SIZE, y*BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), 1)
    # 현재 블록
    shape = game.current_piece['shape']
    color = game.current_piece['color']
    for y, row in enumerate(shape):
        for x, cell in enumerate(row):
            if cell:
                pygame.draw.rect(screen, color, ((game.x+x)*BLOCK_SIZE, (game.y+y)*BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
                pygame.draw.rect(screen, WHITE, ((game.x+x)*BLOCK_SIZE, (game.y+y)*BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), 1)
    # 점수 표시
    font = pygame.font.SysFont('comicsansms', 24)
    score_text = font.render(f"Score: {game.score}", True, WHITE)
    screen.blit(score_text, (10, 10))
    pygame.display.update()

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Tetris - VS Code 최적화")
    clock = pygame.time.Clock()
    game = Tetris()
    drop_event = pygame.USEREVENT + 1
    pygame.time.set_timer(drop_event, 500)  # 블록 자동 하강

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == drop_event:
                game.drop()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    game.move(-1)
                elif event.key == pygame.K_RIGHT:
                    game.move(1)
                elif event.key == pygame.K_DOWN:
                    game.drop()
                elif event.key == pygame.K_UP:
                    game.rotate()
        draw_board(screen, game)
        if game.game_over:
            print(f"Game Over! Final Score: {game.score}")
            running = False
        clock.tick(60)

if __name__ == "__main__":
    main()