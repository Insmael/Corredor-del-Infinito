import pygame

from controler.game_driver import GameDriver


class EventManager:
    """
    clase para administrar los eventos del juego
    """

    def __init__(self):
        self.disable_and_able_events()
        self.menu_event_manager = MenuEventManager()
        self.game_event_manager = GameEventManager()
        self.actual_event_manager = self.menu_event_manager

    def set_in_menu(self):
        """
        cambia el administrador de eventos actual al administrador de eventos de menu
        :return:
        """
        self.actual_event_manager = self.menu_event_manager

    def in_menu(self):
        """
        entrega verdadero si el administrador de eventos de menu es el administrador de eventos actual
        :return:
        """
        return self.actual_event_manager == self.menu_event_manager

    def set_in_game(self):
        """
        cambia el administrador de eventos actual al administrador de eventos de juego
        :return:
        """
        self.actual_event_manager = self.game_event_manager

    def in_game(self):
        """
        entrega verdadero si el administrador de eventos de juego es el administrador de eventos actual
        :return:
        """
        return self.actual_event_manager == self.game_event_manager

    def disable_and_able_events(self):
        """
        deshabilita los eventos que no se ocupan en el juego para que no se llene el event queue con eventos que no
        serán recogidos por los administradores de eventos
        """

        allowed = [pygame.QUIT, pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN, pygame.K_p, pygame.K_m,
                   pygame.K_KP_ENTER]

        pygame.event.set_allowed(None)
        pygame.event.set_allowed(allowed)

    def update(self, game_driver: GameDriver):
        """
        actualiza el juego segun los eventos que ingresa el usuario, los eventos son actualizados desde el gamedriver
        :param game_driver:
        :return:
        """
        event = pygame.event.get(pygame.QUIT)
        if event != None:
            pygame.quit()

        events = pygame.event.get(pygame.KEYDOWN)
        for event in events:
            self.actual_event_manager.handle_keydown_event(event, game_driver)
        events = pygame.event.get(pygame.KEYUP)
        for event in events:
            self.actual_event_manager.handle_keyup_event(event, game_driver)


class MenuEventManager:
    """
    clase que se encarga de coordinar los eventos de menu
    """

    def handle_keydown_event(self, event: pygame.KEYDOWN, game_driver: GameDriver):
        """
        maneja un evento de presionar tecla, actuando sobre la instancia actual del juego
        :param event: el evento de presionar tecla
        :param game_driver: la instancia actual del juego
        :return:
        """
        if event == pygame.K_DOWN:
            game_driver.actual_menu.move_down()
        if event == pygame.K_UP:
            game_driver.actual_menu.move_up()
        if event == pygame.K_RIGHT:
            game_driver.actual_menu.move_right()
        if event == pygame.K_LEFT:
            game_driver.actual_menu.move_left()
        if event == pygame.K_m:
            game_driver.sound_manager.on_off_music()
        if event == pygame.K_KP_ENTER:
            game_driver.actual_menu.go()
        if event == pygame.K_p:
            pass

    def handle_keyup_event(self, event: pygame.KEYUP, game_driver: GameDriver):
        """
        maneja un evento de levantar tecla, actuando sobre la instancia actual del juego
        :param event: el evento de levantar tecla
        :param game_driver: la instancia actual del juego
        :return:
        """
        pass


class GameEventManager:
    """
    clase que se encarga de coordinar los eventos de juego
    """

    def handle_keydown_event(self, event: pygame.KEYDOWN, game_driver: GameDriver):
        """
        maneja un evento de presionar tecla, actuando sobre la instancia actual del juego
        :param event: el evento de presionar tecla
        :param game_driver: la instancia actual del juego
        :return:
        """
        if event == pygame.K_DOWN:
            pass
        if event == pygame.K_UP:
            game_driver.game.jump_straight()
        if event == pygame.K_RIGHT:
            game_driver.game.jump_right()
        if event == pygame.K_LEFT:
            game_driver.game.jump_left()
        if event == pygame.K_m:
            game_driver.sound_manager.on_off_music()
        if event == pygame.K_p:
            game_driver.set_in_pause()
        if event == pygame.K_KP_ENTER:
            pass

    def handle_keyup_event(self, event: pygame.KEYUP, game_driver: GameDriver):
        """
        maneja un evento de levantar tecla, actuando sobre la instancia actual del juego
        :param event: el evento de levantar tecla
        :param game_driver: la instancia actual del juego
        :return:
        """
        if event == pygame.K_DOWN:
            pass
        if event == pygame.K_UP:
            game_driver.game.fall()
        if event == pygame.K_RIGHT:
            game_driver.game.fall()
        if event == pygame.K_LEFT:
            game_driver.game.fall()
        if event == pygame.K_m:
            pass
        if event == pygame.K_p:
            pass
        if event == pygame.K_KP_ENTER:
            pass
