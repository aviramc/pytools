import typeutils

class bunch(object):
    def __init__(self, **kw):
        self.__dict__['attributes'] = kw

    def __repr__(self):
        return self.repr_with_recursion_lock()

    def repr_with_recursion_lock(self, instances=None):
        # TODO: The recursion lock should be better (a list containing a bunch won't really be protected).
        if instances is None:
            instances = []
        if self in instances:
            return "%s(...)" % (self.get_name(), )
        instances.append(self)
        attributes_repr = []
        for key, value in self.attributes.iteritems():
            if isinstance(value, bunch):
                repr_string = value.repr_with_recursion_lock(instances)
            else:
                repr_string = repr(value)
            attributes_repr.append("%s = %s" % (key, repr_string))
        return "%s(%s)" % (self.get_name(), ", ".join(attributes_repr))

    def get_name(self):
        return typeutils.classname(self)

    def __getattr__(self, name):
        if name in self.attributes:
            return self.attributes[name]
        raise AttributeError("'%s' object has no attribute %s" % (self.get_name(), name))

    def __setattr__(self, name, value):
        self.attributes[name] = value

    def __delattr__(self, name):
        if name not in self.attributes:
            raise AttributeError('%s not a member of %s' % (name, self.get_name()))
        self.attributes.pop(name)
