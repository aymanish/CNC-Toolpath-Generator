#include "Circle.h"

// Define M_PI if it's not defined
#ifndef M_PI
#define M_PI 3.14159265358979323846
#endif

Circle::Circle(float radius) : radius(radius) {}

/*
float Circle::getRadius() const // New method to get the radius
{
    return radius;
}
*/

std::vector<sf::Vector2f> Circle::getPoints() const
{
    std::vector<sf::Vector2f> points;
    const int numPoints = 100;
    for (int i = 0; i < numPoints; ++i)
    {
        float angle = (i * 2 * M_PI) / numPoints;
        float x = radius * cos(angle);
        float y = radius * sin(angle);
        points.push_back(sf::Vector2f(x, y));
    }
    return points;
}

void Circle::draw(sf::RenderWindow &window) const
{
    auto points = getPoints();
    for (const auto &point : points)
    {
        sf::CircleShape shape(2); // Small circle to represent the point
        shape.setFillColor(sf::Color::Red);
        // shape.setPosition(point.x + window.getSize().x / 2, point.y + window.getSize().y / 2); // Center the shape
        shape.setPosition(sf::Vector2f(
            point.x + window.getSize().x / 2,
            point.y + window.getSize().y / 2));
        window.draw(shape);
    }
}
