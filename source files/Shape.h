#ifndef SHAPE_H
#define SHAPE_H

#include <SFML/Graphics.hpp>
#include <vector>

// Abstract base class for all shapes
class Shape
{
public:
    virtual ~Shape() = default;
    virtual std::vector<sf::Vector2f> getPoints() const = 0;
    virtual void draw(sf::RenderWindow &window) const = 0;

    virtual float getRadius() const { return 0.0f; } // Default implementation (could be overridden)
};

#endif
