"""Tests for the bundled Toto Washlet Pronto command data."""

import unittest

from custom_components.toto_washlet_ir.const import COMMANDS


class TestCommandData(unittest.TestCase):
    """Validate the command catalog and Pronto payload structure."""

    def test_commands_have_unique_keys(self) -> None:
        keys = [command.key for command in COMMANDS]

        self.assertEqual(len(keys), len(set(keys)))
        self.assertEqual(len(COMMANDS), 12)

    def test_pronto_payloads_match_declared_pair_counts(self) -> None:
        for command in COMMANDS:
            for step in command.steps:
                words = step.pronto.split()
                self.assertEqual(words[0], "0000", command.name)
                pair_count = int(words[2], 16) + int(words[3], 16)
                self.assertEqual(len(words), 4 + 2 * pair_count, command.name)
                self.assertGreaterEqual(step.times, 1, command.name)
