#ifndef CIRCLE_H
#define CIRCLE_H

#include "Shape.h"
#include <cmath>

class Circle : public Shape
{
public:
    Circle(float radius);

    std::vector<sf::Vector2f> getPoints() const override;
    void draw(sf::RenderWindow &window) const override;

    float getRadius() const override { return radius; }

private:
    float radius;
};

#endif
