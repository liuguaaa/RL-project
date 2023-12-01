'''
Function:
	The game over interface
Author:
	Charles
微信公众号:
	Charles的皮卡丘
'''
import sys
import pygame


'''The game over interface'''
def endGame(screen, sounds, showScore, score, number_images, bird, pipe_sprites, backgroud_image, other_images, base_pos, cfg, mode):
	if mode == 'train':
		return
	sounds['die'].play()
	clock = pygame.time.Clock()
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
				pygame.quit()
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE or event.key == pygame.K_UP:
					return
		boundary_values = [0, base_pos[-1]]
		bird.update(boundary_values)
		screen.blit(backgroud_image, (0, 0))
		pipe_sprites.draw(screen)
		screen.blit(other_images['base'], base_pos)
		showScore(screen, score, number_images)
		bird.draw(screen)
		pygame.display.update()
		clock.tick(cfg.FPS)