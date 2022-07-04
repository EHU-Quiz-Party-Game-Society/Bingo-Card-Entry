
# Bingo Card Entry Script

This python script is for current society staff members and allows quicker entry of Bingo cards into the system than the current web portal.

## API Reference

#### Create a new Bingo Card

```http
  POST /bingo/card
```

| Form Data | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `api_key` | `string` | **Required**. Your API key |
| `sheet` | `string` | **Required**. The sheet identifier, usually starting with A |
| `code` | `string` | **Required**. The card identifier, usually starting with M |

## Authors

- [@PenguinNexus](https://www.github.com/PenguinNexus)

