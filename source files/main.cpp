#include <SFML/Graphics.hpp>
#include <iostream>
#include <memory>

#include "Circle.h"
#include "SpiralToolpath.h"

int main()
{
    // Create window
    // sf::RenderWindow window(sf::VideoMode(800, 600), "Toolpath Generator");
    sf::RenderWindow window(sf::VideoMode(sf::Vector2u(800, 600)), "Toolpath Generator");

    // User input to select shape and parameters
    std::cout << "Enter shape type (1 for Circle): ";
    int shapeChoice;
    std::cin >> shapeChoice;

    std::unique_ptr<Shape> shape;

    if (shapeChoice == 1)
    {
        float radius;
        std::cout << "Enter radius of the circle: ";
        std::cin >> radius;
        shape = std::make_unique<Circle>(radius);
    }
    // Add more shapes (e.g., Rectangle) in the future as needed

    // Toolpath generation
    float spacing, theta_step;
    std::cout << "Enter spacing for spiral toolpath: ";
    std::cin >> spacing;
    std::cout << "Enter angular resolution for spiral toolpath: ";
    std::cin >> theta_step;

    SpiralToolpath spiralToolpath(spacing, theta_step);

    while (window.isOpen())
    {
        // sf::Event event;
        // sf::Event event(sf::Event::EventType::None);

        // while (window.pollEvent(event))
        /*
        while (auto eventOpt = window.pollEvent())
        {
            sf::Event event = *eventOpt;

            // if (event.type == sf::Event::Closed)
            //     window.close();
            //  Check event type
            // Close window: exit
            if (event->is<sf::Event::Closed>())
                window.close();
        }
        */

        // Process events
        while (const std::optional event = window.pollEvent())
        {
            // Close window: exit
            if (event->is<sf::Event::Closed>())
                window.close();
        }

        window.clear();
        shape->draw(window);                     // Draw the shape
        spiralToolpath.drawPath(window, *shape); // Draw the toolpath
        window.display();
    }

    return 0;
}
