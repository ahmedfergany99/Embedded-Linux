void LCD_Init(void);

void LCD_WriteCommand(uint8 cmd);

void LCD_WriteData(uint8 data);

int32 LCD_GoTo(uint8 row , uint8 col);

uint8 LCD_WriteString(uint8* str);

char LCD_WriteInteger(sint32 int);

sint32 LCD_Clear(void);

uint8 LCD_off(void);
