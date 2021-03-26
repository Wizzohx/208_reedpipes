NAME = 308reedpipes

RM = rm -f

all: ${NAME}

$(NAME):
	cp 308reedpipes.py ${NAME}
	chmod +x ${NAME}

clean:
	${RM} ${NAME}

fclean:
	${RM} ${NAME}

re: clean all

.PHONY: all re clean fclean
