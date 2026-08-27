import sys
import pygame

from alien import Alien
from bullet import Bullet
from settings import Settings
from ship import Ship


class AlienInvasion:
    """Gerencia o jogo e seus comportamentos."""

    def __init__(self):
        """Construtor da classe que inicializa o jogo e cria os recursos básicos"""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption("Alien Invasion")

        # Criando uma instância da classe Ship para representar a nave espacial
        self.ship = Ship(self.screen, self.settings)

        # Mudando a cor do plano de fundo em RGB
        self.bg_color = self.settings.bg_color

        self.bullets = (
            pygame.sprite.Group()
        )  # Cria um grupo para armazenar os projéteis disparados pela nave

        self.aliens = (
            pygame.sprite.Group()
        )  # Cria um grupo para armazenar os alienígenas presentes no jogo

    def create_fleet(self):
        """Cria uma frota de alienígenas."""
        # Cria um alienígena e calcula o número de alienígenas em uma linha
        # O espaçamento entre os alienígenas é igual a um alienígena
        alien = Alien(self.screen, self.settings)
        alien_width = alien.rect.width
        alien_height = alien.rect.height
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)
        ship_height = self.ship.rect.height
        available_space_y = (
            self.settings.screen_height - (3 * alien_height) - ship_height
        )
        number_rows = available_space_y // (2 * alien_height)

        for row_number in range(number_rows):
            # Cria a primeira linha de alienígenas
            for alien_number in range(number_aliens_x):
                # Cria um alienígena e o posiciona na linha
                alien = Alien(self.screen, self.settings)
                alien.x = alien_width + 2 * alien_width * alien_number
                alien.rect.x = alien.x
                alien.y = alien_height + 2 * alien_height * row_number
                alien.rect.y = alien.y
                self.aliens.add(alien)

        def run_game(self):
            """Cria um laço de repetição para a tela sempre ficar visível até
            que o usuário decida fechar a janela."""

            self.create_fleet()  # Cria a frota de alienígenas para ser desenhada na tela

    
    def _fire_bullet(self) -> None:
        if len(self.bullets) < self.settings.bullet_allowed:
            new_bullet = Bullet(self.screen, self.settings, self.ship)
            self.bullets.add(new_bullet)  
    def _update_bullets(self)-> None:
        self.bullets.update()
        self._remove_offscreen_bullet()
        self._check_bullet_alien_collisions()
    def _remove_offscreen_bullets(self)->None:
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def _check_bullet_alien_collisions(self) -> None:
        pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

    def _update_aliens(self) -> None:
            self._check_fleet_edges()
            self.aliens.update()
    def _check_fleet_edges(self) -> None:
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break
    def _change_fleet_direction(self) -> None:
            """Desce a frota e muda sua direção."""
            for alien in self.aliens.sprites():
                alien.rect.y += self.settings.fleet_drop_speed
            self.settings.fleet_direction *= -1

    def _check_ship_collision(self) -> None:
        """Verifica se a nave colidiu com algum alienígena."""
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            print("A nave foi atingida!")
            sys.exit()

    def _render_screen(self) -> None:
        """Redesenha a tela a cada passagem pelo laço."""
        self.screen.fill(self.bg_color)
        self.ship.blitme()
        self.aliens.draw(self.screen)
        self._draw_bullets()
        pygame.display.flip()

    def _draw_bullets(self) -> None:
        """Desenha os projéteis na tela."""
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

    def _update_game_state(self) -> None:
        """Atualiza a posição da nave, dos projéteis e dos alienígenas."""
        self.ship.update()
        self._update_bullets()
        self._update_aliens()
        self._check_ship_collision()
    def create_fleet(self):
        """Cria uma frota de alienígenas."""
        # Cria um alienígena e calcula o número de alienígenas em uma linha
        # O espaçamento entre os alienígenas é igual a um alienígena
        alien = Alien(self.screen, self.settings)
        alien_width = alien.rect.width
        alien_height = alien.rect.height
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)
        ship_height = self.ship.rect.height
        available_space_y = (
            self.settings.screen_height - (3 * alien_height) - ship_height
        )
        number_rows = available_space_y // (2 * alien_height)

        for row_number in range(number_rows):
            # Cria a primeira linha de alienígenas
            for alien_number in range(number_aliens_x):
                # Cria um alienígena e o posiciona na linha
                alien = Alien(self.screen, self.settings)
                alien.x = alien_width + 2 * alien_width * alien_number
                alien.rect.x = alien.x
                alien.y = alien_height + 2 * alien_height * row_number
                alien.rect.y = alien.y
                self.aliens.add(alien)

    def run_game(self) -> None:
            """Cria um laço de repetição para a tela sempre ficar visível até
            que o usuário decida fechar a janela."""

            self.create_fleet()  # Cria a frota de alienígenas para ser desenhada na tela

            while True:
                self._check_events()
                self._update_game_state()
                self._render_screen()
            if __name__ == "__main__":
                alien_invasion = AlienInvasion()
                alien_invasion.run_game()
class GameEventHandler:
    def __init__(self, ship, bullet_manager):
         self.ship = ship
         self.bullet_manager = bullet_manager
    def _check_events(self) -> None:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KETYDOWN:
                    self._handle_keydown(event)
                elif event.type == pygame.KEYUP:
                    self._handle_keyup(event)
    def _handle_keydown(self,event:pygame.event.Event)-> None:
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
    def _handle_keyup(self,event: pygame.event.Event) -> None:
        if event.key == pygame.K_RIGHT:  
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False     
class BulletManager:
    def __init__(self, screen, settings, ship) -> None:
        self.screen = screen
        self.settings = settings
        self.ship = ship
        self.bullets.add(new_bullet)
    def _update_bullets(self, aliens) -> None:
        self.bullets.update()
        self._remove_offscreen_bullets()
        self._check_bullet_alien_collisions(aliens)
    def _remove_offscreen_bullets(self) -> None:
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
               self.bullets.remove(bullet)
    def _check_bullet_alien_collisions(self,aliens)->None:
        pygame.sprite.groupcollide(self.bullets,aliens,True,True)
class FleetManager:
    def __init__(self,screen,settings,ship)->None:
        self.screen=screen
        self.settings = settings
        self.ship = ship
        self.aliens = pygame.sprite.Group()
    def create_fleet(self):
        alien = Alien(self.screen, self.settings)
        alien_width = alien.rect.width
        alien_height = alien.rect.height
        available_space_x = self.settings.screen_width - (2*alien_width)
        number_aliens_x = available_space_x // (2*alien_width)
        ship_height = self.ship.rect.height
        available_space_y = (
            self.settings.screen_height - (3*alien_height)- ship_height
        )
        number_rows = available_space_y //(2*alien_height)

        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                alien = Alien(self.screen, self.settings)
                alien.x = alien_width + 2*alien_width * alien_number
                alien.rect.x = alien.x
                alien.y = alien_height + 2*alien_height * row_number
                alien.rect.y = alien.y
                self.aliens.add(alien)
    def _update_aliens(self)->None:
        self._check_fleet_edges()
        self.aliens.update()
        self._check_ship_collision()

    def _check_fleet_edges(self)->None:
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction += -1
    def _check_ship_collision(self)->None:
        if pygame.sprite.spritecollideany(self.ship,self.aliens):
            print("A nave foi atingida!")
            sys.exit()
class GameRenderer:
    def _init_(self, screen, bg_color, ship, bullets, aliens) -> None:
        self.screen = screen
        self.bg_color = bg_color
        self.ship = ship
        self.bullets = bullets
        self.aliens = aliens
    def _render_screen(self)->None:
        self.screen.fill(self.bg_color)
        self.ship.blitme()
        self.aliens.draw(self.screen)
        self._draw_bullets()
        pygame.display.flip()
    def _draw_bullets(self)->None:
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
class AlienInvasion:
    def _init_(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self.screen, self.settings)
        self.bg_color = self.settings.bg_color
        self.bullet_manager = BulletManager(self.screen, self.settings, self.ship)
        self.fleet_manager = FleetManager(self.screen, self.settings, self.ship)
        self.event_handler = GameEventHandler(self.ship, self.bullet_manager)
        self.renderer = GameRenderer(
            self.screen,
            self.bg_color,
            self.ship,
            self.bullet_manager.bullets,
            self.fleet_manager.aliens,
        )
    def _update_game_state(self)->None:
        self.ship.update()
        self.bullet_manager._update_bulletss(self.fleet_manager.aliens)
        self.fleet_manager._update_aliens()
    def run_game(self)->None:
        self.fleet_manager.create_fleet()
        while True:
            self.event_handler._check_events()
            self._update_game_state()
            self.renderer._render_screen()
if __name__ == "__main__":
    alien_invasion = AlienInvasion()
    alien_invasion.run_game()
