#ifndef SPIRALTOOLPATH_H
#define SPIRALTOOLPATH_H

#include "Toolpath.h"
#include "Circle.h"
#include <cmath>

class SpiralToolpath : public Toolpath
{
public:
    SpiralToolpath(float spacing, float theta_step);

    std::vector<sf::Vector2f> generatePath(const Shape &shape) const override;
    void drawPath(sf::RenderWindow &window, const Shape &shape) const override;

private:
    float spacing;
    float theta_step;
};

#endif
