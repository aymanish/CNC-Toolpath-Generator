#include "SpiralToolpath.h"
#include "Circle.h"

// Define M_PI if it's not defined
#ifndef M_PI
#define M_PI 3.14159265358979323846
#endif

SpiralToolpath::SpiralToolpath(float spacing, float theta_step)
    : spacing(spacing), theta_step(theta_step) {}

std::vector<sf::Vector2f> SpiralToolpath::generatePath(const Shape &shape) const
{
    const Circle &circle = dynamic_cast<const Circle &>(shape); // Ensure it's a circle
    std::vector<sf::Vector2f> path;
    // float radius = circle.getPoints()[0].x; // Using the circle's radius
    float radius = circle.getRadius(); // Use the getRadius() method
    float k = spacing / (2 * M_PI);
    float theta_max = radius / k;

    for (float theta = 0; theta <= theta_max; theta += theta_step)
    {
        float r = k * theta;
        float x = r * cos(theta);
        float y = r * sin(theta);
        path.push_back(sf::Vector2f(x, y));
    }

    return path;
}

void SpiralToolpath::drawPath(sf::RenderWindow &window, const Shape &shape) const
{
    auto path = generatePath(shape);
    for (const auto &point : path)
    {
        sf::CircleShape shape(2); // Small circle to represent the toolpath point
        shape.setFillColor(sf::Color::Blue);
        // shape.setPosition(point.x + window.getSize().x / 2, point.y + window.getSize().y / 2);
        shape.setPosition(sf::Vector2f(
            point.x + window.getSize().x / 2,
            point.y + window.getSize().y / 2));
        window.draw(shape);
    }
}
