# Toto Washlet IR

A Home Assistant custom integration that adds buttons for Toto Washlet actions
and sends the provided Pronto IR sequences through a Home Assistant infrared
emitter.

## Requirements

- Home Assistant 2026.9 or newer, which provides the `infrared` integration.
- An infrared emitter entity backed by an IR transmitter.
- The transmitter must be aimed at the Washlet and configured for the correct
  IR carrier frequency.

This integration does not connect to a Washlet or report its state. IR is
one-way, so button presses do not confirm that the Washlet received a command.
Compatibility is limited to Washlet models that respond to the IR codes in the
supplied ESPHome YAML.

## Install with HACS

1. In HACS, open **Integrations**, choose the three-dot menu, and select
   **Custom repositories**.
2. Add `https://github.com/alvinchen1/totowashletir` with category **Integration**.
3. Install **Toto Washlet IR** and restart Home Assistant.
4. Go to **Settings → Devices & services → Add integration**, search for
   **Toto Washlet IR**, and select the infrared emitter.

## Buttons

The integration creates buttons for:

- Open Close Seat
- Full Flush and Light Flush
- Stop
- Rear cleansing and Rear soft cleansing
- Front cleansing and Wide front cleansing
- Warm air drying
- Oscillating cleansing and Pulsating cleansing
- Wand clean

Commands that consist of multiple IR transmissions are sent in sequence.
Transmission counts follow the attached ESPHome YAML.

## Icons

Each button has a generic Material Design Icon placeholder in
`custom_components/toto_washlet_ir/icons.json`. Replace those values with Toto
artwork when available.

## Compatibility

The commands are sent as Pronto IR data through Home Assistant's
`InfraredEmitterConsumerEntity` API. IR is one-way, so button presses do not
confirm that the Washlet received a command.

Install this repository through HACS as a custom repository, or copy the
`custom_components/toto_washlet_ir` directory into your Home Assistant
`custom_components` folder.
