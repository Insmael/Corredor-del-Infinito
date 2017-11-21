import pygame


class EventManager:
    """
    clase para administrar los eventos del juego
    """

    def __init__(self):
        self.disable_and_able_events()
        self.in_menu = True

    def disable_and_able_events(self):
        """
        deshabilita los eventos que no se ocupan en el juego para que no se llene el event queue con eventos que no
        serán recogidos por los administradores de eventos
        """

        allowed = [pygame.QUIT, pygame.KEYUP, pygame.KEYDOWN]

        pygame.event.set_allowed(None)
        pygame.event.set_allowed(allowed)

    def update(self, game_driver):
        if self.in_menu:
            self.handle_menu_events(game_driver)
        else:
            self.handle_game_events(game_driver)

    def handle_game_events(self, vista):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT or event.key == pygame.K_ESCAPE:
                pygame.quit()
            if event.key == pygame.K_LEFT and event.type == pygame.KEYDOWN:
                vista.rot_left()
            if event.key == pygame.K_RIGHT and event.type == pygame.KEYDOWN:
                vista.rot_right()
            if event.key == pygame.K_UP and event.type == pygame.KEYDOWN:
                vista.jump_straight()
            if (event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP) \
                    and event.type == pygame.KEYUP:
                vista.fall()

            if event.key == pygame.K_p:
                vista.set_pause()

    def handle_menu_events(self, game_driver):
        """
        maneja un evento de presionar tecla, actuando sobre la instancia actual del juego
        :param event: el evento de presionar tecla
        :param game_driver: la instancia actual del juego
        :return:
        """
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT or event.key == pygame.K_ESCAPE:
                pygame.quit()
            if event.key == pygame.K_DOWN and event.type == pygame.KEYDOWN:
                game_driver.next_menu_item()
            if event.key == pygame.K_UP and event.type == pygame.KEYDOWN:
                game_driver.before_menu_item()
            if event.key == pygame.K_RIGHT and event.type == pygame.KEYDOWN:
                game_driver.next_menu_item()
            if event.key == pygame.K_LEFT and event.type == pygame.KEYDOWN:
                game_driver.before_menu_item()
            if event.key == pygame.K_RETURN and event.type == pygame.KEYDOWN:
                game_driver.select_menu_item()
