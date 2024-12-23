#ifndef TOOLPATH_H
#define TOOLPATH_H

#include "Shape.h"
#include <vector>

class Toolpath
{
public:
    virtual ~Toolpath() = default;
    virtual std::vector<sf::Vector2f> generatePath(const Shape &shape) const = 0;
    virtual void drawPath(sf::RenderWindow &window, const Shape &shape) const = 0;
};

#endif
